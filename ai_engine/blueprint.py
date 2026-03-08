from ai_engine.ai_client import generate_blog_content


def generate_blueprint(topic, pillar, intent):
    """
    Generates a structured content blueprint before the blog is written.
    This helps the AI create deeper, more organized, and less generic articles.
    """

    prompt = f"""
You are a senior SEO strategist and content planner.

Create a structured BLOG BLUEPRINT for the following topic.

Topic: {topic}
Content Pillar: {pillar}
Intent: {intent}

Your job is NOT to write the article.
Your job is to design a strategic outline for a high-ranking SEO blog.

------------------------
OUTPUT STRUCTURE
------------------------

Provide the blueprint using the following sections:

1. Suggested Title

2. Search Intent Explanation
Explain what the reader is looking for when searching this topic.

3. Key Angles To Cover
List 4–6 major perspectives the article should include.

4. Section Structure
Provide the main blog sections:

- Introduction
- Section 1 – Concept explanation
- Section 2 – Why it matters for businesses
- Section 3 – Research insights / statistics
- Section 4 – Step-by-step implementation
- Section 5 – Business impact
- FAQ
- Conclusion

For each section include a short description of what it should contain.

5. Important Statistics To Include
Suggest 3–5 relevant statistics that strengthen the article.

Example sources may include:
Google
HubSpot
Akamai
BrightLocal
Moz

6. Example Expert Insights
Provide 2–3 short realistic expert observations.

Example style:

"In many technical SEO audits, oversized JavaScript bundles are the most common cause of poor Core Web Vitals scores."

7. Semantic SEO Keywords
List related keywords and concepts the article should naturally include.

Example:

Core Web Vitals
page speed optimization
website performance
CDN
lazy loading
image compression

8. FAQ Ideas
Provide 4–5 relevant questions users might ask about this topic.

------------------------
IMPORTANT RULES
------------------------

Keep the blueprint clear and structured.

Do NOT write the full article.

Focus on strategy, structure, and important points.

"""

    return generate_blog_content(prompt, temperature=0.5)