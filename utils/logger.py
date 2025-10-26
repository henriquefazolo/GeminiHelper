import logging
import inspect
from typing import Optional


class Logger:
    def __init__(self, name: Optional[str] = None, log_file: str = '../log.log'):
        if not logging.getLogger().handlers:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',  # Remove %(funcName)s
                handlers=[
                    logging.FileHandler(log_file, encoding='utf-8'),
                    logging.StreamHandler()
                ]
            )

        self.logger_name = name or __name__
        self.logger = logging.getLogger(self.logger_name)

    @staticmethod
    def _get_caller_name():
        frame = inspect.currentframe()
        try:
            caller_frame = frame.f_back.f_back
            return caller_frame.f_code.co_name
        finally:
            del frame

    def info(self, msg: str = ''):
        caller_name = self._get_caller_name()
        self.logger.info(f"{caller_name} - {msg}")

    def warning(self, msg: str):
        caller_name = self._get_caller_name()
        self.logger.warning(f"{caller_name} - {msg}")

    def error(self, msg: Exception | str):
        caller_name = self._get_caller_name()
        self.logger.error(f"{caller_name} - {msg}")

    def critical(self, msg: str):
        caller_name = self._get_caller_name()
        self.logger.critical(f"{caller_name} - {msg}")

    def exception(self, msg: Exception | str):
        caller_name = self._get_caller_name()
        self.logger.exception(f"{caller_name} - {msg}")


if __name__ == '__main__':
    logger = Logger(name='teste')


    def foo():
        try:
            logger.info('1')
        except Exception as e:
            logger.exception(e)
            logger.warning(e)
            logger.critical(e)
            logger.error(e)


    foo()