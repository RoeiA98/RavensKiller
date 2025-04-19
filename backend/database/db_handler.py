import os
from dotenv import load_dotenv
import logging
from backend.server.requests import RequestHandler
from config.config import DREAMLO_PUBLIC_KEY

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".venv", ".env"))
DREAMLO_PRIVATE_KEY = os.getenv("DREAMLO_PRIVATE_KEY")


async def save_score(
    username, score: int, best_time: str, highest_level: int, beat_game: bool
):
    if not all([DREAMLO_PUBLIC_KEY, DREAMLO_PRIVATE_KEY]):
        logging.error("Dreamlo API keys are missing.")
        return {"error": "Dreamlo API keys are missing"}, 500

    url = "http://localhost:8001/submit"

    json_data = {
        "username": username,
        "score": score,
        "best_time": best_time,
        "highest_level": highest_level,
        "beat_game": beat_game,
    }

    dataSend = RequestHandler()
    await dataSend.post(url, json_data)
