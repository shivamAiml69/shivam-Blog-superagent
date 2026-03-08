from ai_engine.ai_client import generate_blog_content


def continue_blog(blog_text):
    """
    If the AI output was truncated, this function asks the model
    to continue writing the remaining sections.
    """

    prompt = f"""
The following article stopped before finishing.

Continue writing the remaining sections naturally.

Do NOT repeat previous sections.

Finish the article completely including:
- remaining sections
- FAQ
- Conclusion

Continue from where the text stopped.

ARTICLE SO FAR:

{blog_text}

Continue writing now.
"""

    continuation = generate_blog_content(prompt, temperature=0.7)

    return blog_text + "\n\n" + continuation