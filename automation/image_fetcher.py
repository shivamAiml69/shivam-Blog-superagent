import os
import requests
import uuid
import base64

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def generate_gemini_image(topic):

    prompt = f"""
    Professional blog hero image about: {topic}.
    Clean minimal modern illustration,
    futuristic technology concept,
    professional blog header image.
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:generateImages?key={GEMINI_API_KEY}"

    payload = {
        "prompt": {
            "text": prompt
        },
        "sampleCount": 1   # ensures only one image
    }

    response = requests.post(url, json=payload)

    data = response.json()

    # get only the first image
    image_base64 = data["images"][0]["bytesBase64Encoded"]

    image_bytes = base64.b64decode(image_base64)

    os.makedirs("temp_images", exist_ok=True)

    file_path = f"temp_images/{uuid.uuid4()}.png"

    with open(file_path, "wb") as f:
        f.write(image_bytes)

    return file_path