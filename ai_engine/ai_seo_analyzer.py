from ai_engine.ai_client import generate_analysis_content

def ai_seo_analysis(blog, topic, pillar, intent):
    """
    High-level SEO & EEAT Audit. 
    Checks if the blog meets the 2026 'Page 1' authority standards.
    """
    prompt = f"""
    Act as a Brutally Honest SEO Auditor. Analyze this blog for the topic: '{topic}'.
    
    AUDIT CRITERIA:
    1. DATA ANCHORING: Does it cite specific (plausible) numbers or case studies?
    2. TECHNICAL DEPTH: Does it mention technical factors (Schema, Core Web Vitals, clustering)?
    3. SEARCH INTENT: Is it a focused guide or just a 'marketing rant'?
    4. UNIQUE INSIGHT: Does it offer a proprietary framework or a 'Hot Take'?
    
    FORMAT:
    Return a JSON-style summary with:
    - Verdict: (Low / Medium / High Ranking Potential)
    - Missing_Signals: (List specific missing data or technical points)
    - Action_Plan: (One sentence on how to fix it)
    
    BLOG TEXT:
    {blog}
    """
    
    # Uses the Flash 2.5 model for high-intelligence analysis
    analysis_raw = generate_analysis_content(prompt)
    return analysis_raw