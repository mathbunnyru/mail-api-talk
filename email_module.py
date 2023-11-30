# Import smtplib for the actual sending function
import smtplib
# Here are the email package modules we'll need
from email.message import EmailMessage
# Secure connection to SMTP Server
import ssl
# File handling
from pathlib import Path


def send_message_from_yandex(sender_email, password, msg):
    SMTP_PORT = 465  # For SSL
    SMTP_SERVER = "smtp.yandex.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg)


def main():
    sender_email = "mathbunnyru@yandex.ru"

    # Create the container email message
    msg = EmailMessage()
    msg['Subject'] = 'Awesome email with attached image'
    msg['From'] = sender_email
    msg['To'] = sender_email

    # Open the file in binary mode
    msg.add_attachment(
        (Path.home() / ".talk" / "image.jpeg").read_bytes(),
        maintype='image',
        subtype='jpeg'
    )

    password = (Path.home() / ".talk" / "yandex_mail_app_pass").read_text()
    send_message_from_yandex(
        sender_email=sender_email,
        password=password,
        msg=msg,
    )


if __name__ == "__main__":
    main()
