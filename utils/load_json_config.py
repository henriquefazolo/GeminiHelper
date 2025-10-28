import json
from utils.logger import Logger


def load_json_config(json_file, logger: Logger = Logger(name=f'{__name__}', log_file='../log.log')):
    try:
        logger.info('star')
        with open(json_file) as file:
            json_data = json.load(file)

        logger.info('end')
        return json_data
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    test = load_json_config(json_file=r'../config/config.json')