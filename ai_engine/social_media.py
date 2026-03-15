from google import genai
import os

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def generate_social_posts(title, summary):

    prompt = f"""
Create social media posts from this blog.

Blog Title:
{title}

Blog Summary:
{summary}

Return two sections:

INSTAGRAM POST
- Hook in first line
- Short paragraphs
- Emojis
- 8–12 hashtags

LINKEDIN POST
- Professional tone
- Bullet points
- End with a discussion question
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text