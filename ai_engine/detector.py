def get_ai_score(text):
    """
    Internal scoring logic to identify AI fingerprints.
    Analyzes vocabulary usage and structural symmetry to provide 
    a 'robotic probability' score.
    """
    # Start with a baseline score
    score = 40
    
    # 1. Check for Robotic Vocabulary (AI "Tells")
    # These terms are common in standard LLM outputs and raise flags.
    robotic_terms = [
        "delve", "tapestry", "furthermore", "moreover", 
        "in today's world", "in the digital age", "unleash", "embark"
    ]
    
    for term in robotic_terms:
        if term in text.lower():
            score += 12 # Penalize for each robotic term found
            
    # 2. Structural Symmetry Check
    # AI models often generate paragraphs of very similar lengths.
    # Human writing is naturally 'bursty' with high variation in length.
    paragraphs = text.split('\n\n')
    if len(paragraphs) > 2:
        lengths = [len(p) for p in paragraphs]
        # If the difference between the longest and shortest paragraph is small,
        # it suggests robotic uniformity.
        if max(lengths) - min(lengths) < 150:
            score += 15 # Penalize for excessive symmetry
            
    # 3. Final Score Normalization
    # We cap the score at 98% to avoid perfection in the critic's eyes.
    return min(score, 98)