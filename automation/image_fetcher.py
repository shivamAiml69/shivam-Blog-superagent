import os
import requests
import uuid
import base64

FLUX_API_KEY = os.getenv("FLUX_API_KEY")

def generate_blog_image(topic):

    prompt = f"""
    Professional blog hero image about: {topic}.
    Clean minimal modern illustration,
    futuristic technology concept,
    professional blog header image.
    """

    url = "https://upadhyayshivamaiml-9216-resource.services.ai.azure.com/providers/blackforestlabs/v1/flux-2-pro?api-version=preview"

    headers = {
        "Authorization": f"Bearer {FLUX_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "FLUX.2-pro",
        "prompt": prompt,
        "width": 1024,
        "height": 1024,
        "n": 1
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Flux API Error: {response.text}")

    data = response.json()

    image_base64 = data["data"][0]["b64_json"]
    image_bytes = base64.b64decode(image_base64)

    os.makedirs("temp_images", exist_ok=True)

    file_path = f"temp_images/{uuid.uuid4()}.png"

    with open(file_path, "wb") as f:
        f.write(image_bytes)

    return file_path