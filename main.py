# main.py
import asyncio
from PIL import ImageGrab
from utils.listener_keyboard import ListenerKeyboard
from utils.screenshot_clipboard import screenshot_to_clipboard
from utils.logger import Logger
from utils.gemini_services import gemini_service_account
from utils.send_msg_to_webhook import send_msg_to_webhook
from utils.load_json_config import load_json_config
from utils.parse_gemini_response import parse_gemini_response

logger = Logger(name=f'{__name__}', log_file='log.log')

json_config = load_json_config(r'config/config.json', logger=Logger(name=f'{__name__}', log_file='log.log'))

webhook = json_config.get('webhook')
google_genai_secret_file = json_config.get('google_genai_secret_file')
gemini_model = json_config.get('gemini_model')

shutdown_application_keys = json_config.get('shutdown_application_keys')
callback_screenshot_to_gemini_keys = json_config.get("callback_screenshot_to_gemini_keys")

logger.info(webhook)
logger.info(google_genai_secret_file)
logger.info(gemini_model)
logger.info(shutdown_application_keys)
logger.info(callback_screenshot_to_gemini_keys)

running = True


async def screenshot_to_gemini(event):
    try:
        clipboard_success = await screenshot_to_clipboard(event, logger=Logger(name=f'{__name__}', log_file='log.log'))

        imagem = ImageGrab.grabclipboard()

        if clipboard_success:
            prompt = """
            You are an expert AI Exam Solver specialized in visual analysis of multiple-choice questions.

            ### INSTRUCTIONS
            1. Analyze the provided image, paying attention to the visual layout to distinguish the question from the alternatives.
            2. Extract the text of the question and all alternatives (A, B, C, D, E).
            3. Think step-by-step to determine the correct answer based on factual knowledge.
            4. Output the result strictly in the XML format defined below.

            ### RESPONSE FORMAT
            <root>
              <reasoning>
                [Briefly explain why the correct alternative is correct and why others are wrong. This ensures accuracy.]
              </reasoning>
              <text>
                QUESTÃO: [Question Number or "N/A"]
                RESPOSTA: [Letter] - [Text of the correct alternative]
              </text>
            </root>

            ### ERROR HANDLING
            - If the image is completely unreadable: <text>IMAGEM ILEGÍVEL</text>
            - If it is not a question: <text>QUESTÃO NÃO IDENTIFICADA</text>

            ### EXAMPLE
            User Image: 
            Assistant Output:
            <root>
              <reasoning>
                The question asks for 5 + 5. Option A is 8, Option B is 10. 10 is the correct sum.
              </reasoning>
              <text>
                QUESTÃO: 5
                RESPOSTA: B - 10
              </text>
            </root>

            ### TASK
            Analyze the image provided by the user and output only the <root> XML block.
            """

            gemini_service = gemini_service_account(credentials=google_genai_secret_file, genai_model=gemini_model,
                                                    logger=Logger(name=f'{__name__}', log_file='log.log'))

            logger.info(f'Using {gemini_service.model_name}')

            result = gemini_service.generate_content([prompt, imagem])

            clean_output = parse_gemini_response(result.text)
            send_msg_to_webhook(webhook, message=clean_output,
                                logger=Logger(name=f'{__name__}', log_file='log.log'))

    except Exception as e:
        logger.exception(e)


def shutdown_application(event):
    global running
    logger.info("Finalizando aplicação")
    running = False


def callback_screenshot_to_gemini(event):
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            loop.create_task(screenshot_to_gemini(event))
        else:
            asyncio.run(screenshot_to_gemini(event))
    except RuntimeError:
        asyncio.run(screenshot_to_gemini(event))


async def main():
    global running

    listener = ListenerKeyboard(logger=Logger(name=f'{__name__}', log_file='log.log'))

    for key in callback_screenshot_to_gemini_keys:
        listener.add_callback(key_name=key, callback=callback_screenshot_to_gemini)

    for key in shutdown_application_keys:
        listener.add_callback(key_name=key, callback=shutdown_application)

    await listener.start()

    try:
        logger.info("🚀 Aplicação iniciada!")
        logger.info(f"📸 Capturar screenshot → Gemini {gemini_model}\n{callback_screenshot_to_gemini_keys}")
        logger.info(f"🔴 Finalizar aplicação\n{shutdown_application_keys}")
        send_msg_to_webhook(webhook, message=f"🤖 *Gemini Agent Online*\nModel: `{gemini_model}`",
                            logger=Logger(name=f'{__name__}', log_file='log.log'))

        # ✅ Loop controlado pela flag
        while running:
            await asyncio.sleep(0.2)  # ✅ Sleep menor para resposta mais rápida

    except KeyboardInterrupt:
        logger.info("⚠️ Programa interrompido pelo usuário (Ctrl+C)")
    finally:
        logger.info("🛑 Finalizando listener...")
        listener.stop()
        send_msg_to_webhook(webhook, message="✅ Aplicação finalizada!",
                            logger=Logger(name=f'{__name__}', log_file='log.log'))
        logger.info("✅ Aplicação finalizada!\n\n")


if __name__ == "__main__":
    asyncio.run(main())