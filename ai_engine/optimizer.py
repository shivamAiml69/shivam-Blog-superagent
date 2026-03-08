from ai_engine.ai_client import generate_blog_content

def improve_blog(blog, readability, score):

    prompt = f"""
Improve the clarity and flow of the following blog.

Do NOT shorten it.
Do NOT rewrite entirely.
Only improve sentence clarity and transitions.

Current Readability: {readability}
Current SEO Score: {score}

BLOG:
{blog}
"""

    return generate_blog_content(prompt, temperature=0.6)