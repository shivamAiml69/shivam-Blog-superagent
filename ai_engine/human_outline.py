from ai_engine.ai_client import generate_blog_content


def generate_human_outline(topic, pillar):
    """
    Generates rough human-style planning notes before writing the article.
    This reduces AI detection patterns.
    """

    prompt = f"""
You are a marketing strategist preparing rough notes for a blog article.

Topic: {topic}
Content Pillar: {pillar}

Write messy planning notes like a human brainstorming ideas.

Rules:
• bullet points
• incomplete thoughts allowed
• short notes
• practical examples
• mention possible statistics
• mention possible sections

Do NOT write the full article.

Write brainstorming notes only.
"""

    outline = generate_blog_content(prompt, temperature=0.8)

    return outline