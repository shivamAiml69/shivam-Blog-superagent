import os
import requests
import uuid
import base64
from io import BytesIO
from PIL import Image
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# -----------------------------------
# Environment
# -----------------------------------

FLUX_API_KEY = os.getenv("FLUX_API_KEY")

# Ensure image folder exists
os.makedirs("temp_images", exist_ok=True)

# -----------------------------------
# Persistent session (faster on Render)
# -----------------------------------

session = requests.Session()

retry_strategy = Retry(
    total=3,
    backoff_factor=1,
    status_forcelist=[429, 500, 502, 503, 504]
)

adapter = HTTPAdapter(max_retries=retry_strategy)

session.mount("https://", adapter)
session.mount("http://", adapter)

# -----------------------------------
# Flux Image Generator
# -----------------------------------

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
        "n": 2
    }

    try:

        response = session.post(
            url,
            headers=headers,
            json=payload,
            timeout=60
        )

        print("Flux status:", response.status_code)

        if response.status_code != 200:
            print("Flux API error:", response.text)
            return None

        data = response.json()

        if "data" not in data:
            print("Invalid Flux response:", data)
            return None

        # Try each generated image
        for img in data["data"]:

            image_base64 = img.get("b64_json")

            if not image_base64:
                continue

            image_bytes = base64.b64decode(image_base64)

            # Skip tiny/corrupt images
            if len(image_bytes) < 1000:
                print("Skipping corrupted image")
                continue

            # -----------------------------------
            # Validate image using Pillow
            # -----------------------------------

            try:
                image = Image.open(BytesIO(image_bytes))
                image.verify()
            except Exception as e:
                print("Invalid image data:", e)
                continue

            # Determine extension
            format = image.format.lower()

            if format not in ["png", "jpeg", "jpg"]:
                format = "png"

            file_path = f"temp_images/{uuid.uuid4()}.{format}"

            with open(file_path, "wb") as f:
                f.write(image_bytes)

            print("Valid image generated:", file_path)

            return file_path

        print("No valid image found")
        return None

    except Exception as e:

        print("Flux generation error:", e)
        return None