from google import genai
import time
from ai_engine.setting import GEMINI_KEYS
from ai_engine.usage_tracker import log_token_usage


# -----------------------------------
# KEY MANAGEMENT SYSTEM
# -----------------------------------

BLOCKED_KEYS = {}
KEY_USAGE = {key: 0 for key in GEMINI_KEYS}

COOLDOWN_SECONDS = 60


def is_key_available(key):
    """Check if key is currently blocked."""

    if key not in BLOCKED_KEYS:
        return True

    blocked_time = BLOCKED_KEYS[key]

    if time.time() - blocked_time > COOLDOWN_SECONDS:
        del BLOCKED_KEYS[key]
        return True

    return False


def block_key(key):
    """Temporarily block a key."""
    BLOCKED_KEYS[key] = time.time()


def get_sorted_keys():
    """
    Load balancing:
    least-used key first
    """

    available_keys = [
        key for key in GEMINI_KEYS
        if is_key_available(key)
    ]

    # If all keys blocked, wait and retry
    if not available_keys:
        print("All keys temporarily blocked. Waiting for cooldown...")
        time.sleep(COOLDOWN_SECONDS)
        return GEMINI_KEYS

    return sorted(
        available_keys,
        key=lambda k: KEY_USAGE.get(k, 0)
    )


# -----------------------------------
# FAILOVER + LOAD BALANCING ENGINE
# -----------------------------------

def generate_with_failover(model_name, prompt, generation_config):

    last_error = None

    sorted_keys = get_sorted_keys()

    for key in sorted_keys:

        try:

            genai.configure(api_key=key)

            model = genai.GenerativeModel(model_name)

            response = model.generate_content(
                prompt,
                generation_config=generation_config
            )

            # Track usage for load balancing
            KEY_USAGE[key] += 1

            # Safe token logging
            if hasattr(response, "usage_metadata"):
                log_token_usage(
                    model_name,
                    response.usage_metadata.prompt_token_count,
                    response.usage_metadata.candidates_token_count
                )

            return response.text

        except Exception as e:

            error_text = str(e).lower()

            # Detect quota / rate errors
            if any(word in error_text for word in ["quota", "rate", "limit", "429"]):

                print(f"Rate limit detected → blocking key: {key}")
                block_key(key)

            else:

                print(f"Key failed: {key}")

            last_error = e

    print("All Gemini keys failed.")
    raise last_error


# -----------------------------------
# BLOG GENERATION
# -----------------------------------

def generate_blog_content(prompt, temperature=0.75):

    return generate_with_failover(
        "models/gemini-2.5-flash-lite",
        prompt,
        {
            "temperature": temperature,
            "max_output_tokens": 2000
        }
    )


# -----------------------------------
# ANALYSIS ENGINE
# -----------------------------------

def generate_analysis_content(prompt, temperature=0.7):

    return generate_with_failover(
        "models/gemini-2.5-flash",
        prompt,
        {
            "temperature": temperature,
            "max_output_tokens": 1600
        }
    )


# -----------------------------------
# AI DETECTION CRITIC
# -----------------------------------

def get_ai_critic_score(text):
    """
    High-sensitivity critic.
    Forces the writer to stay below 35% by penalizing common AI patterns.
    """

    prompt = f"""
 Act as a professional AI detection algorithm. Analyze the following text. 
    Be EXTREMELY critical. Flag any text that:
    1. Uses perfectly balanced sentence structures.
    2. Has a 'predictable' flow or standard business transitions.
    3. Feels too helpful or sterile.
    
    Return ONLY a raw number from 1 to 100. 
    If you see standard AI rhythms, give it a score above 60.
    TEXT: {text}
"""

    response = generate_with_failover(
        "models/gemini-2.5-flash",
        prompt,
        {
            "temperature": 0.1,
            "max_output_tokens": 10
        }
    )

    try:
        score_text = response.strip()
        return int(''.join(filter(str.isdigit, score_text)))

    except:
        return 50