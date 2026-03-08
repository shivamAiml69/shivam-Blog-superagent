import json
import os
from datetime import datetime

USAGE_FILE = "api_usage.json"

def log_token_usage(model_name, prompt_tokens, candidate_tokens):
    """Tracks token consumption for Developer View."""
    today = datetime.now().strftime("%Y-%m-%d")
    
    if not os.path.exists(USAGE_FILE):
        data = {}
    else:
        with open(USAGE_FILE, "r") as f:
            data = json.load(f)

    if today not in data:
        data[today] = {"total_tokens": 0, "models": {}, "blogs_created": 0}

    if model_name not in data[today]["models"]:
        data[today]["models"][model_name] = {"prompt": 0, "completion": 0}

    data[today]["models"][model_name]["prompt"] += prompt_tokens
    data[today]["models"][model_name]["completion"] += candidate_tokens
    data[today]["total_tokens"] += (prompt_tokens + candidate_tokens)
    
    # Increment blog count only when the writer model finishes
    if "flash-lite" in model_name:
        data[today]["blogs_created"] += 1

    with open(USAGE_FILE, "w") as f:
        json.dump(data, f, indent=4)