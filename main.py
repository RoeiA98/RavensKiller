import asyncio
import pygame
from LevelsDesign.LevelsHandler import LevelsHandler

if __name__ == "__main__":
    pygame.init()
    # game = GameLevels()
    game = LevelsHandler()
    asyncio.run(game.run_game())
