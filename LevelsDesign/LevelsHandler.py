import pygame # type: ignore
import asyncio
import importlib
import os
from Game.levels import GameLevels
from SpritesLogic.player import Player
from UI.levels import Levels

class LevelsHandler(GameLevels):

    def __init__(self):
        super().__init__()

        self.levels = [None]  # Initialize with None for index 0
        levels_dict = {}

        # Dynamically import all modules in the LevelsDesign folder
        levels_design_path = os.path.dirname(__file__)
        for filename in os.listdir(levels_design_path):
            if filename.endswith(".py") and filename != "__init__.py" and filename != "LevelsHandler.py" and filename != "scenes.py":
                module_name = f"LevelsDesign.{filename[:-3]}"
                module = importlib.import_module(module_name)
                # Assuming each module has a class with the same name as the file
                class_name = filename[:-3]
                levels_dict[f"{class_name}"] = module
        
        sorted_dict = dict(sorted(levels_dict.items())) # Sorting levels in ascending order
        for class_name, module in sorted_dict.items():
            self.levels.append(getattr(module, class_name))

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
                self.handler()
            elif self.continue_screen:
                self.load_next_level()
            else:
                self.game_over()
                self.game_restart()

            pygame.display.update()
            self.fps.clock.tick(self.MAX_FPS)
            await asyncio.sleep(0)
