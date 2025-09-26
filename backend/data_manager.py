import json
from pathlib import Path

DATA_FILE = Path("backend/data/movies.json")

def load_movies():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_movies(movies):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(movies, f, indent=4)
