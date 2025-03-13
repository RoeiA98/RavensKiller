import pygame
import asyncio
from src.Game.run import GameRun
from backend.server.server import start_server

async def main():
    pygame.init()
    game = GameRun()

    # running game and server concurrently
    await asyncio.gather(
        game.run_game(),
        start_server()
    )

if __name__ == "__main__":
    asyncio.run(main())