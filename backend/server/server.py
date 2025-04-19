from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from pydantic import BaseModel
import logging
from backend.server.requests import RequestHandler
from utils.utils import time_to_centiseconds
from config.config import DREAMLO_API_URL
from dotenv import load_dotenv
import os

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".venv", ".env"))
DREAMLO_PRIVATE_KEY = os.getenv("DREAMLO_PRIVATE_KEY")
DREAMLO_PUBLIC_KEY = os.getenv("DREAMLO_PUBLIC_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or restrict to your domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ScoreRequest(BaseModel):
    username: str
    score: int
    best_time: str
    highest_level: int
    beat_game: bool


@app.post("/submit")
async def submit_score(data: ScoreRequest):
    try:
        # Validate and convert best_time
        best_time_int = time_to_centiseconds(data.best_time)
    except ValueError:
        logging.error(f"Invalid best_time format: {data.best_time}")
        raise HTTPException(
            status_code=422, detail="Invalid best_time format. Expected HH:MM:SS.ss"
        )

    if not all([DREAMLO_PUBLIC_KEY, DREAMLO_PRIVATE_KEY]):
        logging.error("Dreamlo API keys are missing.")
        raise HTTPException(status_code=500, detail="Dreamlo API keys are missing")

    url = f"{DREAMLO_API_URL}/{DREAMLO_PRIVATE_KEY}/add/{data.username}/{data.score}/{best_time_int}"

    params = {"text": "Game Beaten" if data.beat_game else "Not Beaten"}

    try:
        dataSend = RequestHandler()
        await dataSend.get(url, params=params)
    except Exception as e:
        logging.error(f"Dreamlo submission failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Dreamlo submission failed")

    return {"status": "success"}


async def start_server():
    config = uvicorn.Config(app, host="127.0.0.1", port=8001, log_level="debug")
    server = uvicorn.Server(config)
    await server.serve()
