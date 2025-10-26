import json
from utils.logger import Logger

logger = Logger(name=f'{__name__}', log_file='log.log')


def load_json_config(json_file):
    logger.info('star')
    with open(json_file) as file:
        json_data = json.load(file)

    logger.info('end')
    return json_data
