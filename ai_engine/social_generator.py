import google.generativeai as genai
import os
import time
from ai_engine.setting import GEMINI_KEYS


def generate_social_posts(title, summary):

    prompt = f"""
Create two sections.

INSTAGRAM POST:
- Hook in first line
- Short paragraphs
- Emojis
- 8-12 hashtags

LINKEDIN POST:
- Professional tone
- Bullet points
- End with a discussion question

Topic:
{title}

Blog Summary:
{summary}
"""

    # Try each key until one works
    for key in GEMINI_KEYS:
        try:
            genai.configure(api_key=key)
            model = genai.GenerativeModel("models/gemini-1.5-flash")
            response = model.generate_content(prompt)
            if response.text:
                return response.text

        except Exception as e:
            print(f"Social generator key failed: {e}")
            time.sleep(2)
            continue

    print("All keys failed for social generation")
    return ""