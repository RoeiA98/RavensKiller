# TESTS/test_levels_handler.py
import unittest
import sys
import os
import asyncio
import pygame
from unittest.mock import patch, AsyncMock

# Set work directory to the root directory of the project
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Add the root directory to the Python path
sys.path.append(os.getcwd())
from src.Game.handler import Handler


class TestLevelsHandler(unittest.TestCase):

    def setUp(self):
        pygame.init()
        self.game = Handler()

    def tearDown(self):
        pygame.quit()

    def test_initial_state(self):
        self.assertIsNotNone(self.game)
        self.assertIsInstance(self.game, Handler)

    def test_run_game(self):
        with patch(
            "Game.LevelsHandler.LevelsHandler.run_game", new_callable=AsyncMock
        ) as mock_run_game:
            asyncio.run(self.game.run_game())
            mock_run_game.assert_called_once_with()

    # def test_enemy_spawning(self):
    #     # Assuming LevelsHandler has a method spawn_enemies
    #     with patch('Game.LevelsHandler.LevelsHandler.spawn_enemies') as mock_spawn_enemies:
    #         self.game.spawn_enemies()
    #         mock_spawn_enemies.assert_called_once()

    # def test_player_movement(self):
    #     # Assuming LevelsHandler has a method handle_player_movement
    #     with patch('Game.LevelsHandler.LevelsHandler.handle_player_movement') as mock_handle_player_movement:
    #         self.game.handle_player_movement()
    #         mock_handle_player_movement.assert_called_once()


if __name__ == "__main__":
    unittest.main()
