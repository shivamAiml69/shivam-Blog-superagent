from tavily import TavilyClient
from setting import TAVILY_API_KEY
from datetime import datetime
import random
import re

# Import your Gemini failover engine
from ai_engine.ai_client import generate_analysis_content


# -----------------------------
# API Setup
# -----------------------------

tavily = TavilyClient(api_key=TAVILY_API_KEY)


# -----------------------------
# Clean Output
# -----------------------------

def clean_output(text):

    topics = []

    for line in text.split("\n"):

        line = line.strip()

        if not line:
            continue

        line = re.sub(r"^\d+[\.\)]\s*", "", line)
        line = line.replace("*", "")

        if len(line) < 8:
            continue

        topics.append(line)

    return topics


# -----------------------------
# Tavily Topic Signals
# -----------------------------

def tavily_signals(pillar):

    year = datetime.now().year

    query = f"""
    latest {pillar} digital marketing strategies and trends {year}
    """

    try:

        response = tavily.search(
            query=query,
            search_depth="advanced",
            max_results=6
        )

        results = response.get("results", [])

        signals = [
            r.get("title")
            for r in results
            if r.get("title")
        ]

        return signals

    except Exception as e:

        print("Tavily error:", e)
        return []


# -----------------------------
# Gemini Topic Generator
# -----------------------------

def generate_topics(pillar, intent, custom_topic=None):

    signals = tavily_signals(pillar)

    signal_text = "\n".join(signals)

    topic_focus = custom_topic if custom_topic else pillar

    prompt = f"""
You are an expert digital marketing strategist.

Generate 5 long-tail SEO blog titles.

Content Pillar:
{pillar}

Content Intent:
{intent}

Primary Topic:
{topic_focus}

Market signals from the web:
{signal_text}

Requirements:

- Titles must match real Google search queries
- Use long-tail SEO keywords (8–14 words)
- Focus on digital marketing strategies
- Align titles with the intent: {intent}
- Avoid generic titles
- Do not include placeholders like [city]
- Make titles actionable and practical
- Return only titles
- One title per line
- Use year {datetime.now().year} if relevant
"""

    try:

        # Use failover Gemini engine
        response = generate_analysis_content(prompt)

        topics = clean_output(response)

        return topics

    except Exception as e:

        print("Gemini error:", e)
        return []


# -----------------------------
# Main Function
# -----------------------------

def suggest_topics(pillar, intent, custom_topic=None):

    topics = generate_topics(pillar, intent, custom_topic)

    random.shuffle(topics)

    return "\n".join(
        f"{i+1}. {t}" for i, t in enumerate(topics[:5])
    )