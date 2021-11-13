import os
import smtplib
import requests
import time
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()

BOT_EMAIL_ADDRESS = os.getenv('BOT_EMAIL')
EMAIL_PASSWORD = os.getenv('BOT_PSW')
TO_EMAIL_ADDRESS = os.getenv('TO_EMAIL')
URL = os.getenv('URL')
SLEEP_INTERVAL = 60

email = EmailMessage()
email['from'] = 'Email Bot'
email['to'] = TO_EMAIL_ADDRESS
email['subject'] = 'Automated Message - Site Down'

while True:
    response = requests.get(URL, timeout=5)
    if response.status_code != 200:
        email.set_content(f'No 200 response from {URL}. Recieved status code {response.status_code} instead.')
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.ehlo()
            connection.starttls()
            connection.login(user=BOT_EMAIL_ADDRESS, password=EMAIL_PASSWORD)
            connection.send_message(email)
    time.sleep(SLEEP_INTERVAL)