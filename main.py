# main.py
import asyncio
from PIL import ImageGrab
from utils.listener_keyboard import ListenerKeyboard
from utils.screenshot_clipboard import screenshot_to_clipboard
from utils.logger import Logger
from utils.gemini_services import gemini_service_account
from utils.send_msg_to_webhook import send_msg_to_webhook
from utils.load_json_config import load_json_config

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
            prompt = """Você é um assistente especializado em análise de questões de múltipla escolha.

            TAREFA: Analise a imagem e resolva a questão apresentada.

            INSTRUÇÕES OBRIGATÓRIAS:
            1. Extraia TODO o texto visível da imagem
            2. Identifique claramente a pergunta principal
            3. Liste todas as alternativas disponíveis (A, B, C, D, E, etc.)
            4. Analise logicamente cada alternativa em relação à pergunta
            5. Determine a alternativa correta com base em conhecimento factual

            FORMATO DE RESPOSTA OBRIGATÓRIO:
            <text>
            NUMERO DA QUESTÃO: [número da questão, se houver]
            RESPOSTA CORRETA: [alternativa, se houver + texto da alternativa]
            </text>

            REGRAS IMPORTANTES:
            - Se não conseguir identificar a questão, informe "QUESTÃO NÃO IDENTIFICADA"
            - Se a imagem estiver ilegível, informe "IMAGEM ILEGÍVEL"
            - Seja preciso e objetivo na resposta
            - Base sua análise em fatos, não em suposições
            - Não retorne o texto de analise da questão.
            - Retorne unicamente o formato obrigatorio na tag <text>
            """

            gemini_service = gemini_service_account(credentials=google_genai_secret_file, genai_model=gemini_model,
                                                    logger=Logger(name=f'{__name__}', log_file='log.log'))

            logger.info(f'Using {gemini_service.model_name}')

            result = gemini_service.generate_content([prompt, imagem])

            send_msg_to_webhook(webhook, f'```{result.text.replace('<text>', '').replace('</text>', '')}```',
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
        logger.info(f"📸 Capturar screenshot → Gemini\n{callback_screenshot_to_gemini_keys}")
        logger.info(f"🔴 Finalizar aplicação\n{shutdown_application_keys}")

        # ✅ Loop controlado pela flag
        while running:
            await asyncio.sleep(0.2)  # ✅ Sleep menor para resposta mais rápida

    except KeyboardInterrupt:
        logger.info("⚠️ Programa interrompido pelo usuário (Ctrl+C)")
    finally:
        logger.info("🛑 Finalizando listener...")
        listener.stop()
        logger.info("✅ Aplicação finalizada!\n\n")


if __name__ == "__main__":
    asyncio.run(main())