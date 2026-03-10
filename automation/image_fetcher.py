"""
Unsplash image fetcher.
Searches for a relevant photo based on the blog topic/pillar,
downloads it locally, and returns the file path.
"""

import requests
import os
from ai_engine.setting import UNSPLASH_ACCESS_KEY


def fetch_image(topic: str, pillar: str) -> str | None:
    """
    Search Unsplash for a relevant image and download it.
    Returns local file path on success, None on failure.
    """

    # Build a smart search query from topic + pillar
    query = _build_query(topic, pillar)

    try:
        # Search Unsplash
        resp = requests.get(
            "https://api.unsplash.com/search/photos",
            params={
                "query":       query,
                "per_page":    1,
                "orientation": "landscape",
                "content_filter": "high",
            },
            headers={"Authorization": f"Client-ID {UNSPLASH_ACCESS_KEY}"},
            timeout=10,
        )
        resp.raise_for_status()
        data = resp.json()

        results = data.get("results", [])
        if not results:
            print(f"[Unsplash] No results for query: {query}")
            return None

        photo     = results[0]
        image_url = photo["urls"]["regular"]   # ~1080px wide
        photo_id  = photo["id"]

        # Download the image
        img_resp = requests.get(image_url, timeout=20)
        img_resp.raise_for_status()

        os.makedirs("temp_images", exist_ok=True)
        file_path = f"temp_images/{photo_id}.jpg"

        with open(file_path, "wb") as f:
            f.write(img_resp.content)

        print(f"[Unsplash] Downloaded: {file_path}")
        return file_path

    except Exception as e:
        print(f"[Unsplash] Error: {e}")
        return None


def _build_query(topic: str, pillar: str) -> str:
    """
    Build a concise, visual search query.
    Long blog titles don't search well on Unsplash.
    """
    # Pillar → best visual keyword mapping
    pillar_map = {
        "Digital Marketing": "digital marketing business",
        "Astrology":         "stars astrology cosmos",
        "Finance":           "finance money business",
        "Business":          "business strategy office",
        "Health":            "health wellness lifestyle",
        "Technology":        "technology innovation",
        "Education":         "education learning",
        "Legal":             "law legal justice",
        "Real Estate":       "real estate property",
        "Travel":            "travel landscape adventure",
        "Local SEO":         "local business street",
        "Lead Gen":          "business meeting growth",
        "AI Strategy":       "artificial intelligence tech",
        "Social Media Marketing": "social media smartphone",
        "Website Optimization":   "website design laptop",
    }

    base = pillar_map.get(pillar, pillar)

    # Extract first 3–4 meaningful words from topic
    words = [w for w in topic.split() if len(w) > 3][:3]
    if words:
        return f"{base} {' '.join(words)}"

    return base
