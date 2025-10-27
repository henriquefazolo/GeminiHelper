import google.generativeai as genai
from google.oauth2 import service_account
from PIL import ImageGrab
from utils.logger import Logger

logger = Logger()

def gemini_service_account(credentials, genai_model='gemini-2.5-flash-lite'):

    credentials_path = credentials

    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['https://www.googleapis.com/auth/generative-language']
    )

    genai.configure(credentials=credentials)
    return genai.GenerativeModel(genai_model)


if __name__ == "__main__":
    from screenshot_clipboard import screenshot_to_clipboard
    import asyncio


    async def run():
        await screenshot_to_clipboard(None)

    asyncio.run(run())

    imagem = ImageGrab.grabclipboard()

    credentials_path_input = r''
    gemini_service = gemini_service_account(credentials_path_input)
    logger.info(f'Using {gemini_service.model_name}')

    prompt = "extraia o texto da imagem."
    response = gemini_service.generate_content([prompt, imagem])

    print(response.text)
