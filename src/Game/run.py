import pygame
import asyncio
from src.Game.handler import Handler
from src.Game.game_state import GameState


class GameRun(Handler):

    def __init__(self):
        super().__init__()

    async def run_game(self):
        while True:
            print(self.state_manager.current_state)
            while self.state_manager.is_state(GameState.INTRO):
                print(self.state_manager.current_state)
                await self.game_intro.intro_screen_menu()
                intro_result = await self.game_intro.handle_game_intro_events()
                if intro_result:
                    self.state_manager.change_state(GameState.PLAYING)
                pygame.display.update()
                await asyncio.sleep(0)

            self.start_time = pygame.time.get_ticks()

            while not self.state_manager.is_state(GameState.INTRO):
                print(self.state_manager.current_state)
                if self.state_manager.is_state(GameState.PLAYING):
                    self.game_handler()
                elif self.state_manager.is_state(GameState.PAUSED):
                    self.handle_pause_state()
                elif self.state_manager.is_any_state(GameState.GAME_OVER, GameState.NEXT_LEVEL, GameState.DISPLAY_OBJECTIVE, GameState.FINAL_SCREEN):
                    self.game_stop()

                pygame.display.update()
                self.fps.clock.tick(self.MAX_FPS)
                await asyncio.sleep(0)