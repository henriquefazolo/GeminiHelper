from utils.logger import Logger
import requests
import json


def send_msg_to_webhook(webhook_link, message, logger:Logger = Logger(name=f'{__name__}', log_file=r'log.log')):
    try:
        logger.info('start')

        payload = {
            "text": message
        }

        headers = {
            "Content-Type": "application/json"
        }

        response = requests.post(
            webhook_link,
            data=json.dumps(payload),
            headers=headers,
            timeout=30  # Timeout de 30 segundos
        )
        logger.info(str(response.status_code))
        logger.info('end')

    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    from utils.load_json_config import load_json_config

    webhook = load_json_config(r'../config/config.json').get('webhook')

    send_msg_to_webhook(webhook, 'oi')
