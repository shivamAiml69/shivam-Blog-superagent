import requests
import os

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")


def send_message(chat_id, text):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    requests.post(url, json=payload)


def send_photo(chat_id, image_path):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto"

    files = {
        "photo": open(image_path, "rb")
    }

    data = {
        "chat_id": chat_id
    }

    requests.post(url, files=files, data=data)