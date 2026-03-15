import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel( "models/gemini-2.5-flash-lite")

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

    try:

        response = model.generate_content(prompt)

        if response.text:
            return response.text

        return ""

    except Exception as e:

        print("Social generation error:", e)

        return ""