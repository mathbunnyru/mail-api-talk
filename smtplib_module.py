#!/usr/bin/env python3
# Import smtplib for the actual sending function
import smtplib

# Secure connection to SMTP Server
import ssl

# File handling
from pathlib import Path


def send_message_from_yandex(
    sender_email: str,
    password: str,
    receiver_email: str,
    message: str,
) -> None:
    SMTP_PORT = 465  # For SSL
    SMTP_SERVER = "smtp.yandex.com"

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)


def main() -> None:
    message = """\
Subject: Such a nice subject

Please, verify, that the body is correct."""

    sender_email = "mathbunnyru@yandex.ru"
    receiver_email = sender_email
    password = (Path.home() / ".talk" / "yandex_mail_app_pass").read_text()
    send_message_from_yandex(
        sender_email=sender_email,
        password=password,
        receiver_email=receiver_email,
        message=message,
    )


if __name__ == "__main__":
    main()
