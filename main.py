import asyncio
import pygame # type: ignore
from src.Game.handler import Handler

if __name__ == "__main__":
    pygame.init()
    game = Handler()

    asyncio.run(game.run_game())