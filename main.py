import asyncio
import pygame # type: ignore
from src.Game.run import GameRun

if __name__ == "__main__":
    pygame.init()
    game = GameRun()

    asyncio.run(game.run_game())