from ai_engine.ai_client import generate_blog_content

def reduce_ai_pattern(blog, retry=False, last_score=0):
    """
    Rewrites content to reduce AI detection patterns while preserving
    a professional business tone suitable for client-facing blogs.
    """

    feedback = ""
    if retry:
        feedback = f"""
        The previous version was flagged as {last_score}% AI-generated.
        Increase sentence variation and paragraph diversity while
        maintaining a professional tone.
        """

    prompt = f"""
Act as a professional copy editor improving human writing patterns
while keeping the article suitable for a professional business blog.

{feedback}

STRICT EDITING RULES:

1. SENTENCE VARIATION
Ensure natural variation in sentence structure.
Avoid repeating sentence openings such as "The", "This", or "It".

2. PARAGRAPH VARIATION
Ensure paragraph lengths vary naturally.
Avoid perfectly symmetrical paragraphs.

3. WORD CHOICE DIVERSITY
Replace repetitive or predictable wording with
contextually accurate alternatives.

4. REMOVE AI TEMPLATES
Remove phrases such as:
"In the digital age"
"it's crucial to"
"in today's fast-paced world"

5. LIST NATURALIZATION
If bullet lists look overly uniform,
convert one or two items into short narrative explanations.

6. EMPHASIS SENTENCES
Occasionally add short emphasis sentences (5–8 words) to improve rhythm.

Example:
"This step is often overlooked."
"Many businesses miss this detail."

7. MAINTAIN PROFESSIONAL TONE
Keep the tone professional, clear, and suitable for a business audience.
Avoid slang, casual expressions, or exaggerated language.

IMPORTANT:
Do not significantly shorten the article.
Keep all SEO keywords and headings intact.

ARTICLE:
{blog}
"""

    temp = 0.9 if not retry else 0.95

    return generate_blog_content(prompt, temperature=temp)