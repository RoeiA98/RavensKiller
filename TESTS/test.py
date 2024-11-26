# TESTS/test_levels_handler.py
import unittest
import sys
import os
import pygame  # type: ignore

# Change the working directory to the root directory of the project
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Add the root directory to the Python path
sys.path.append(os.getcwd())

from Game.LevelsHandler import LevelsHandler

class TestLevelsHandler(unittest.TestCase):

    def setUp(self):
        pygame.init()  # Initialize Pygame
        self.game = LevelsHandler()

    def tearDown(self):
        pygame.quit()  # Quit Pygame

    def test_initial_state(self):
        self.assertIsNotNone(self.game)
        # Add more assertions to test the initial state of LevelsHandler

    def test_run_game(self):
        # Test the run_game method
        # You might need to mock dependencies or use a test framework that supports async tests
        pass

if __name__ == '__main__':
    unittest.main()