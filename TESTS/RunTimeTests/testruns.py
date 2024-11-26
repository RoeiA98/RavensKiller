import sys
import os

# Change the working directory to the root directory of the project
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

# Add the root directory to the Python path
sys.path.append(os.getcwd())

import asyncio
import pygame  # type: ignore
import unittest
from Game.LevelsHandler import LevelsHandler
from TESTS.RunTimeTests.enemiestests import EnemiesTests

async def run_tests_periodically(enemies_test):
    while True:
        enemies_test.show_current_enemies()
        await asyncio.sleep(1)  # Run the test every second

async def main():
    pygame.init()
    game = LevelsHandler()
    enemies_test = EnemiesTests(game)
    
    # Run the tests periodically
    asyncio.create_task(run_tests_periodically(enemies_test))
    
    # Run the game
    await game.run_game()

if __name__ == "__main__":
    asyncio.run(main())
