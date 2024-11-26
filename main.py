import asyncio
import pygame # type: ignore
from Game.LevelsHandler import LevelsHandler

if __name__ == "__main__":
    pygame.init()
    game = LevelsHandler()

    asyncio.run(game.run_game())