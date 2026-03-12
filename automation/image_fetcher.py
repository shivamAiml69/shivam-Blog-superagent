import os
import requests
import uuid
import base64

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
FLUX_API_KEY = os.getenv("FLUX_API_KEY")

IMAGE_MODEL = os.getenv("IMAGE_MODEL", "gemini")


def generate_gemini_image(topic):

    prompt = f"""
    Professional blog hero image about: {topic}.
    Clean minimal modern illustration,
    futuristic technology concept,
    professional blog header image.
    """

    url = f"https://generativelanguage.googleapis.com/v1beta/models/imagen-3.0-generate-002:generateImages?key={GEMINI_API_KEY}"

    payload = {
        "prompt": {"text": prompt},
        "sampleCount": 1
    }

    response = requests.post(url, json=payload)
    data = response.json()

    image_base64 = data["images"][0]["bytesBase64Encoded"]
    image_bytes = base64.b64decode(image_base64)

    os.makedirs("temp_images", exist_ok=True)

    file_path = f"temp_images/{uuid.uuid4()}.png"

    with open(file_path, "wb") as f:
        f.write(image_bytes)

    return file_path


def generate_flux_image(topic):

    prompt = f"""
    Professional blog hero image about: {topic}.
    Clean minimal modern illustration,
    futuristic technology concept,
    professional blog header image.
    """

    url = "https://upadhyayshivamaiml-9216-resource.services.ai.azure.com/providers/blackforestlabs/v1/flux-2-pro?api-version=2024-12-01-preview"

# Use your actual key here"

    headers = {
        "Authorization": f"Bearer {FLUX_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": prompt,
        "width": 1024,
        "height": 1024
    }

    response = requests.post(url, headers=headers, json=payload)

    data = response.json()

    image_url = data["image"]

    image_bytes = requests.get(image_url).content

    os.makedirs("temp_images", exist_ok=True)

    file_path = f"temp_images/{uuid.uuid4()}.png"

    with open(file_path, "wb") as f:
        f.write(image_bytes)

    return file_path


def generate_blog_image(topic):

    if IMAGE_MODEL == "flux":
        return generate_flux_image(topic)
    else:
        return generate_gemini_image(topic)