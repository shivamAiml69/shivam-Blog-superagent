import requests
import os

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def generate_social_posts(title, summary):

    prompt = f"""
Create social media posts from this blog.

Blog Title:
{title}

Blog Summary:
{summary}

Return two sections:

INSTAGRAM POST:
- Hook in first line
- Short paragraphs
- Emojis
- 8-12 hashtags

LINKEDIN POST:
- Professional tone
- Bullet points
- End with a discussion question
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={GEMINI_API_KEY}"

    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    r = requests.post(url, json=payload)

    data = r.json()

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except:
        return "Social post generation failed"