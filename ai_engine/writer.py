from ai_engine.ai_client import generate_blog_content

def generate_blog(topic, pillar, intent):
    """
    Final optimized writer using the Authority + Professional SEO protocol.
    Produces structured, research-backed, client-ready blogs.
    """

    intent_map = {
        "educational": "Educate clearly with technical depth and step-by-step explanations.",
        "conversion": "Persuade readers by addressing pain points and offering data-backed solutions.",
        "authority": "Demonstrate expertise using frameworks, analysis, and industry insight.",
        "seo": "Focus on semantic keyword coverage and search ranking strategy.",
        "engagement": "Write in a compelling, relatable style that encourages reader interaction."
    }

    intent_description = intent_map.get(intent, "Provide professional insight and educational value.")

    banned_words = [
        "delve", "tapestry", "unleash", "embark",
        "comprehensive", "robust", "harness",
        "ever-evolving", "foster", "testament",
        "in conclusion", "moreover", "furthermore",
        "unlocking", "tailored", "paving the way",
        "look no further"
    ]

    prompt_text = f"""
You are a professional SEO strategist and business consultant writing for a company blog.

Your writing must feel like it was written by an experienced industry professional, not an AI system.

Topic: {topic}
Content Pillar: {pillar}
Intent: {intent_description}

-------------------------
PROFESSIONAL WRITING RULES
-------------------------

WORD COUNT
Write approximately 1500–1600 words.

TONE
Professional
Business-focused
Educational
Clear and practical

Do NOT use slang, exaggerated marketing language, or hype.

Avoid phrases such as:
"game changer"
"revolutionary"
"unlock the power"
"in today's digital age"
"ever-evolving landscape"

Do NOT use these banned words:
{', '.join(banned_words)}

-------------------------
AUTHORITY & EEAT SIGNALS
-------------------------

Each major section should include at least one of the following:

• Industry statistics  
• Research references  
• Practical examples  
• Small case studies  

Example:

"Research from Google indicates that pages loading within two seconds can reduce bounce rates by more than 20 percent."

Include at least one realistic case example.

Example:

"A mid-sized SaaS company improved page speed from 4.1 seconds to 2.2 seconds after optimizing images and implementing CDN delivery. Within three months, organic traffic increased by 17 percent."

Mention technical elements when relevant such as:

Core Web Vitals  
Schema markup  
semantic search  
E-E-A-T signals  
structured data  

-------------------------
EXPERT INSIGHT RULE
-------------------------

Include 2–3 short expert observations throughout the article.

These should sound like practical insights gained from real experience.

Examples:

"In many technical SEO audits, the most common performance issue isn't server speed but oversized JavaScript bundles."

"In many local SEO audits, the most common ranking issue isn't backlinks but incomplete Google Business Profile information."

"Many small businesses invest heavily in ads but overlook conversion tracking, which limits their ability to measure marketing ROI."

These observations should feel natural and practical, not promotional.

-------------------------
STYLE
-------------------------

Write like a consultant explaining concepts to business leaders.

Use:

clear explanations  
structured sections  
practical insights  
evidence-based analysis  

Avoid:

generic filler  
AI-style transitions  
overly promotional language  

-------------------------
SENTENCE VARIATION
-------------------------

Use natural variation in sentence length.

Some sentences should be short and direct.

Others can be longer and analytical.

Paragraph lengths should vary to avoid robotic patterns.

Avoid repeating sentence openings.

Occasionally include a short emphasis sentence (5–8 words).

Examples:

"This changes everything for local SEO."

"Most businesses miss this step."

-------------------------
SEMANTIC SEO
-------------------------

Naturally include related concepts connected to the topic.

Example for Local SEO:

Google Business Profile  
local search rankings  
customer reviews  
map pack visibility  
local citations  

Use them naturally within the article.

-------------------------
STRUCTURE
-------------------------

Follow this exact structure:

Title

Meta Description

Introduction

Section 1 – Concept explanation

Section 2 – Why the topic matters for businesses

Section 3 – Research insights or industry statistics

Section 4 – Step-by-step implementation strategy

Section 5 – Business impact and practical benefits

FAQ Section (4–5 relevant questions)

Conclusion

-------------------------
HUMAN WRITING SIGNALS
-------------------------

Occasionally include:

• one-sentence emphasis paragraphs
• brief practical observations
• contrast sentences

Examples:

Most businesses overlook this step.

Landing page optimization is not only about design. It is about user psychology.

Many companies spend thousands on ads.

But they forget the page where the visitor lands.

-------------------------
IMPORTANT
-------------------------

Do NOT start with phrases like:

"Here is the article"
"Certainly"
"Sure"

Start directly with the Title.

Write the full article now.
"""

    return generate_blog_content(prompt_text)