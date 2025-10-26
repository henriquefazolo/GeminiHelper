from utils.logger import Logger
import requests
import json


def send_msg_to_webhook(webhook_link, message):
    logger = Logger(name=f'{__name__}')

    try:
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

    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':

    webhook = 'https://chat.googleapis.com/v1/spaces/AAQAvzJTL4o/messages?key=AIzaSyDdI0hCZtE6vySjMm-WEfRq3CPzqKqqsHI&token=OvzIn5y76TH9CUvSihc_JFnuVbM6DjkZ8nz0s14hhd0'

    send_msg_to_webhook(webhook, 'oi')
