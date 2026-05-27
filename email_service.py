import time
import smtplib
from email.mime.text import MIMEText

from config import *
from template import *
from logger import *

def send_email(subject, items):

    html_content = build_email_template(items)

    msg = MIMEText(html_content, "html", "utf-8")

    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = ", ".join(TO_EMAILS)

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()

        server.login(EMAIL_USER, EMAIL_PASS)

        server.send_message(msg)

def send_notification_email(subject, items, max_retries=3, delay=15):
    last_error = None

    for attempt in range(1, max_retries + 1):

        try:
            logger.info(f"Sending e-mail attempt {attempt}/{max_retries}")
            send_email(subject, items)
            return True

        except smtplib.SMTPException as e:
            last_error = e
            logger.warning(f"SMTP error on attempt {attempt}: {e}")

        except Exception:
            logger.exception(f"Unexpected error on attempt {attempt}")

        if attempt < max_retries:
            sleep_time = delay * attempt
            logger.info(f"Retrying sending e-mail in {sleep_time}s...")
            time.sleep(sleep_time)

    logger.error(f"Failed to send email after {max_retries} attempts: {last_error}")
    return False