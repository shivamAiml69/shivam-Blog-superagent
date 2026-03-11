import requests
import os

# Telegram Bot Token from Render Environment
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"


# -----------------------------------
# SEND TEXT MESSAGE
# -----------------------------------

def send_message(chat_id, text):

    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text
    }

    try:

        response = requests.post(url, json=payload)

        print("Telegram sendMessage:", response.text)

    except Exception as e:

        print("Telegram send_message error:", e)


# -----------------------------------
# SEND INLINE BUTTONS
# -----------------------------------

def send_buttons(chat_id, text, buttons):

    """
    buttons format example:

    [
        [{"text": "Button1", "callback_data": "data1"}],
        [{"text": "Button2", "callback_data": "data2"}]
    ]
    """

    url = f"{BASE_URL}/sendMessage"

    payload = {
        "chat_id": chat_id,
        "text": text,
        "reply_markup": {
            "inline_keyboard": buttons
        }
    }

    try:

        response = requests.post(url, json=payload)

        print("Telegram buttons:", response.text)

    except Exception as e:

        print("Telegram send_buttons error:", e)


# -----------------------------------
# SEND PHOTO
# -----------------------------------

def send_photo(chat_id, image_path):

    url = f"{BASE_URL}/sendPhoto"

    try:

        with open(image_path, "rb") as photo:

            files = {"photo": photo}

            data = {"chat_id": chat_id}

            response = requests.post(url, files=files, data=data)

            print("Telegram photo:", response.text)

    except Exception as e:

        print("Telegram send_photo error:", e)


# -----------------------------------
# EDIT MESSAGE (OPTIONAL)
# -----------------------------------

def edit_message(chat_id, message_id, text):

    url = f"{BASE_URL}/editMessageText"

    payload = {
        "chat_id": chat_id,
        "message_id": message_id,
        "text": text
    }

    try:

        response = requests.post(url, json=payload)

        print("Telegram editMessage:", response.text)

    except Exception as e:

        print("Telegram edit_message error:", e)


# -----------------------------------
# ANSWER CALLBACK (IMPORTANT)
# -----------------------------------

def answer_callback(callback_id):

    """
    Prevents Telegram loading spinner
    """

    url = f"{BASE_URL}/answerCallbackQuery"

    payload = {
        "callback_query_id": callback_id
    }

    try:

        requests.post(url, json=payload)

    except Exception as e:

        print("Callback answer error:", e)