import asyncio
import io
import sys
import win32clipboard
import win32con
from utils.logger import Logger
from PIL import ImageGrab


async def screenshot_to_clipboard(event, logger: Logger = Logger(name=f'{__name__}', log_file='../log.log')):
    try:
        logger.info('start')
        screenshot = ImageGrab.grab()
        if sys.platform == "win32":
            output = io.BytesIO()
            screenshot.convert('RGB').save(output, 'BMP')
            data = output.getvalue()[14:]

            win32clipboard.OpenClipboard()
            win32clipboard.EmptyClipboard()
            win32clipboard.SetClipboardData(win32con.CF_DIB, data)
            win32clipboard.CloseClipboard()
            logger.info('end')
            return True

    except Exception as e:
        logger.exception(e)

if __name__ == '__main__':
    async def run():
        await screenshot_to_clipboard(None)

    asyncio.run(run())