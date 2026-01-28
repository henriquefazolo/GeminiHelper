import requests
from PIL import ImageGrab
from utils.logger import Logger
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def gemini_service_api_key(api_key, prompt_text, image_b64, genai_model='gemini-2.5-flash-lite',
                           logger: Logger = Logger(name=f'{__name__}', log_file='../log.log')):
    try:
        logger.info('start')

        url = f"https://generativelanguage.googleapis.com/v1beta/models/{genai_model}:generateContent?key={api_key}"

        headers = {'Content-Type': 'application/json'}

        # Estrutura exata que o Gemini espera via REST
        payload = {
            "contents": [{
                "parts": [
                    {"text": prompt_text},
                    {
                        "inline_data": {
                            "mime_type": "image/jpeg",
                            "data": image_b64
                        }
                    }
                ]
            }]
        }
        response = requests.post(url, headers=headers, json=payload, verify=False)

        if response.status_code == 200:
            result = response.json()
            # Extraindo o texto da resposta
            return result['candidates'][0]['content']['parts'][0]['text']
        else:
            return response.text
    except Exception as e:
        logger.exception(e)
    finally:
        logger.info('end')


if __name__ == "__main__":
    from screenshot_clipboard import screenshot_to_clipboard
    from image_to_base64 import image_to_base64
    import asyncio
    from utils.load_json_config import load_json_config

    json_config = load_json_config(r'../config/config.json', logger=Logger(name=f'{__name__}', log_file='log.log'))

    api_key = json_config.get('api_key')

    async def run():
        await screenshot_to_clipboard(None)

    asyncio.run(run())

    imagem = ImageGrab.grabclipboard()
    image_b64 = image_to_base64(imagem)



    prompt = "extraia o texto da imagem."
    response = gemini_service_api_key(api_key=api_key, prompt_text=prompt, image_b64=image_b64)

    print(response)
