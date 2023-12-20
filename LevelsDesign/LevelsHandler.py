from GameOrigin.GameLevels import GameLevels
from LevelsDesign.Level1 import LevelOne
import pygame
import asyncio
from LevelsDesign.Level2 import LevelTwo
from LevelsDesign.Level3 import LevelThree
from LevelsDesign.Level4 import LevelFour
from Sprites.Player import Player
from UI.Levels import *


class LevelsHandler(GameLevels):

    def __init__(self):
        super().__init__()

        self.levels = [
            None,
            LevelOne,
            LevelTwo,
            LevelThree,
            LevelFour
        ]

    def handler(self):
        self.levels[self.current_level].play(self)

    async def run_game(self):

        while not self.game_running:
            self.game_scenes.game_intro()
            self.game_running = self.game_start()
            pygame.display.update()
            await asyncio.sleep(0)

        self.game_active_status = True
        self.player.add(Player())  # player draw

        while self.game_running:
            if self.game_active_status:
                # print(self.collisions.ground_raven_damage)
                self.handler()
            elif self.continue_screen:
                self.load_next_level()
            else:
                # End game and reset levels
                self.game_over()
                self.game_restart()

            pygame.display.update()
            self.fps.clock.tick(self.MAX_FPS)
            await asyncio.sleep(0)

