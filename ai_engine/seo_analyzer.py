import textstat
import re
from collections import Counter
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

stop_words = set(stopwords.words("english"))

# -------------------------
# Readability
# -------------------------

def readability_score(text):
    return round(textstat.flesch_reading_ease(text), 2)


# -------------------------
# Keyword Density
# -------------------------

def keyword_density(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    filtered = [w for w in words if w not in stop_words and len(w) > 3]
    total = len(filtered)

    if total == 0:
        return {}

    counts = Counter(filtered)

    return {
        word: round((count / total) * 100, 2)
        for word, count in counts.most_common(10)
    }


# -------------------------
# SEO Score
# -------------------------

def seo_score(text):
    score = 0

    read = readability_score(text)
    word_count = len(text.split())
    density = keyword_density(text)

    # 🔹 Readability (30 points)
    # Scales gradually instead of harsh buckets
    score += min(30, max(10, int(read / 2)))

    # 🔹 Content Length (20 points)
    if word_count >= 1200:
        score += 20
    elif word_count >= 900:
        score += 15
    elif word_count >= 600:
        score += 10
    else:
        score += 5

    # 🔹 Heading Structure (20 points)
    if "##" in text:
        score += 10
    if "###" in text:
        score += 5
    if "FAQ" in text or "Frequently Asked Questions" in text:
        score += 5

    # 🔹 Keyword Coverage (15 points)
    score += min(15, len(density) * 2)

    # 🔹 CTA Presence (15 points)
    if any(word in text.lower() for word in [
        "contact", "get started", "book a call", "learn more"
    ]):
        score += 15

    return min(score, 100)