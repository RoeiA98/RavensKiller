# /// script
# requires-python = ">=3.12"
# dependencies = [
#   "pygame-ce"
# ]
# ///
import pygame
import asyncio
from src.Game.run import GameRun


async def main():
    pygame.init()
    game = GameRun()

    await asyncio.gather(game.run_game())


if __name__ == "__main__":
    asyncio.run(main())
