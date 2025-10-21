import os
# from dotenv import load_dotenv
import logging
from backend.server.requests import RequestHandler
from utils.Utils import load_env_file

env_path = os.path.join(os.path.dirname(__file__), "..", "..", ".venv", ".env")
load_env_file(env_path)

DREAMLO_PRIVATE_KEY = os.environ.get("DREAMLO_PRIVATE_KEY")
DREAMLO_PUBLIC_KEY = os.environ.get("DREAMLO_PUBLIC_KEY")

# uncomment for pygbag to work with dreamlo
# DREAMLO_PUBLIC_KEY="67fe4d868f40bb05a0d24049"
# DREAMLO_PRIVATE_KEY="WMVQQa__VEy2fNLcWUWhfAL_MNAPmzUk-dVqKWiw3drg"


async def save_score(username, score: int, best_time: str, highest_level: int, beat_game: bool):
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
