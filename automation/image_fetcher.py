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

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=60)

        print("Flux status:", response.status_code)

        if response.status_code != 200:
            print("Flux error:", response.text)
            return None

        data = response.json()

        if "data" not in data:
            print("Invalid response:", data)
            return None

        image_base64 = data["data"][0].get("b64_json")

        if not image_base64:
            print("Empty image returned")
            return None

        image_bytes = base64.b64decode(image_base64)

        # Validate PNG header
        if not image_bytes.startswith(b'\x89PNG'):
            print("Invalid PNG image")
            return None

        os.makedirs("temp_images", exist_ok=True)

        file_path = f"temp_images/{uuid.uuid4()}.png"

        with open(file_path, "wb") as f:
            f.write(image_bytes)

        return file_path

    except Exception as e:
        print("Flux error:", e)
        return None