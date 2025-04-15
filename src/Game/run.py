# /// script
# dependencies = [
#     "pymongo"
# ]
# ///

import pygame
import asyncio
from game.handler import Handler
import pymongo

class GameRun(Handler):
    
    def __init__(self):
        super().__init__()
    
    async def run_game(self):
        print("test outside")
        while True:
            print("test inside")
            while not self.game_running:
                self.game_intro.intro_screen_menu()
                self.game_running = self.game_intro.handle_game_intro_events()
                pygame.display.update()
                await asyncio.sleep(0)

            self.game_active_status = True
            self.start_time = pygame.time.get_ticks()
            
            while self.game_running:
                if self.game_active_status:
                    self.game_handler()
                else:
                    self.game_stop()

                pygame.display.update()
                self.fps.clock.tick(self.MAX_FPS)
                await asyncio.sleep(0)