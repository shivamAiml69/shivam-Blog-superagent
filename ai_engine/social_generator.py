from ai_engine.ai_client import generate_analysis_content


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

        result = generate_analysis_content(prompt)

        if result:
            return result

        return ""

    except Exception as e:

        print("Social generation error:", e)

        return ""