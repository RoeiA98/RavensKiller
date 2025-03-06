from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import os
from backend.database.db_handler import save_score  # Import the save_score function
import uvicorn

# Load environment variables from .env file
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.venv', '.env'))

app = FastAPI()

class ScoreRequest(BaseModel):
    username: str
    score: int
    best_time: str
    highest_level: int
    beat_game: bool

@app.post("/save_score")
async def save_score_api(score_request: ScoreRequest):
    """API route to save score (this can be used for HTTP requests)."""
    response, status_code = save_score(
        score_request.username,
        score_request.score,
        score_request.best_time,
        score_request.highest_level,
        score_request.beat_game
    )
    if status_code == 200:
        return response
    else:
        raise HTTPException(status_code=status_code, detail=response["error"])

async def start_server():
    config = uvicorn.Config(app, host="127.0.0.1", port=5000, log_level="debug")
    server = uvicorn.Server(config)
    await server.serve()
