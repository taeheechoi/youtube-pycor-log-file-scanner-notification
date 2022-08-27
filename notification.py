import json
import logging
import os

import requests
from dotenv import load_dotenv

load_dotenv()

WEBHOOK_URL = os.getenv('WEBHOOK_URL')


class Notification:

    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}

    def send_notification(self, text):
        message = '*Notification using Webhook*\n{text}}'  # *(asterisk) to make title bold

        data = json.dumps({'text': text})
        
        response = requests.post(WEBHOOK_URL, data=data, headers=self.headers)

        if response.status_code == 200:
            logging.info(f'"{text}" has been sent successfully.')
        else:
            logging.info(f'Error: Sending {text} has been failed due to {response.reason}')


if __name__ == '__main__':
    logging.basicConfig(filename='log/notification.txt', format='%(asctime)s %(message)s', level=logging.INFO)

    notification = Notification()
    notification.send_notification('Have a good day!')
