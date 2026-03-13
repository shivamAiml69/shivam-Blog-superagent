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
        "n": 2   # 🔥 generate 2 images instead of 1
    }

    try:

        response = requests.post(url, headers=headers, json=payload, timeout=60)

        print("Flux status:", response.status_code)

        if response.status_code != 200:
            print("Flux API error:", response.text)
            return None

        data = response.json()

        if "data" not in data:
            print("Invalid Flux response:", data)
            return None

        os.makedirs("temp_images", exist_ok=True)

        # 🔥 try each generated image
        for img in data["data"]:

            image_base64 = img.get("b64_json")

            if not image_base64:
                continue

            image_bytes = base64.b64decode(image_base64)

            # Skip corrupted images
            if len(image_bytes) < 1000:
                print("Skipping invalid image")
                continue

            file_path = f"temp_images/{uuid.uuid4()}.png"

            with open(file_path, "wb") as f:
                f.write(image_bytes)

            print("Valid image generated:", file_path)

            return file_path

        print("No valid image found")
        return None

    except Exception as e:

        print("Flux generation error:", str(e))

        return None