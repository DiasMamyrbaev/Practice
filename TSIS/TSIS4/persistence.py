import json
import os

SETTINGS_FILE = "settings.json"
LEADERBOARD_FILE = "leaderboard.json"

def load_settings():
    default_settings = {"sound": True, "difficulty": "Normal", "car_color": "Red"}
    if not os.path.exists(SETTINGS_FILE):
        save_settings(default_settings)
        return default_settings
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)

def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)

def save_score_json(username, score, time_survived):
    scores = load_leaderboard_json()
    scores.append({"username": username, "score": score, "time": time_survived})
    scores = sorted(scores, key=lambda x: (-x['score'], x['time']))[:10]
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(scores, f, indent=4)

def load_leaderboard_json():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)
    


