from pydantic import BaseModel

class ScoreRequest(BaseModel):
    username: str
    score: int
    best_time: str
    highest_level: int
    beat_game: bool