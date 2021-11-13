This script will send a `GET` request to a specified URL every 60 seconds, and it will send an email to a specified email address if the status code of the response is not `200`.

## Setup

This script uses `dotenv` to retrieve the email credentials the bot will login to, email to send the message to, and the URL to check. Create a file named `.env` with the following content:

```
BOT_EMAIL="email_address_to_send_from"
BOT_PSW="password_for_above_email_address"
TO_EMAIL="email_to_send_email_to"
URL="url_to_check_the_status_of"
```

You could also hardcode these values in `main.py` by replacing the values of these constants with the desired credentials and URL:

```
BOT_EMAIL_ADDRESS = os.getenv('BOT_EMAIL')
EMAIL_PASSWORD = os.getenv('BOT_PSW')
TO_EMAIL_ADDRESS = os.getenv('TO_EMAIL')
URL = os.getenv('URL')
```