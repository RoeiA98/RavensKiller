import pygame  # type: ignore
import asyncio
from src.Game.handler import Handler
from src.Sprites.player import Player


class GameRun(Handler):
    
    def __init__(self):
        super().__init__()
    
    async def run_game(self):
        while True:
            while not self.game_running:
                # self.game_intro.display_intro()
                self.game_intro.intro_screen_menu()
                self.game_running = self.game_intro.handle_game_intro_events()
                pygame.display.update()
                await asyncio.sleep(0)

            self.game_active_status = True
            self.player.add(Player())  # player draw
            self.start_time = pygame.time.get_ticks()

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