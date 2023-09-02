import asyncio
import pygame
from LevelsDesign.GameLevels import GameLevels

if __name__ == "__main__":
    pygame.init()
    game = GameLevels()
    asyncio.run(game.run_game())
