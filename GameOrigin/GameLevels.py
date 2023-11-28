import pygame

from GameOrigin.Modes import GameModes
from UI.FPS import FPS
from UI.Levels import *


class GameLevels(GameModes):

    def __init__(self):
        super().__init__()

        self.keys = pygame.key.get_pressed()
        self.game_font = pygame.font.Font('Fonts/Amatic-Bold.ttf', 40)
        self.level_text = None
        self.objective_text = None
        self.objective_text_rect = None
        self.progress_text = None
        self.progress_text_rect = None
        self.level_text_rect = None
        self.objective2_text = None
        self.objective2_text_rect = None
        self.fps = FPS()

    def stop_level(self):
        self.continue_screen = True
        self.game_active_status = False
        self.current_level += 1

    def load_next_level(self):

        if self.current_level >= len(self.game_level_scenes):
            self.game_scenes.final_scene(self.display_player_score.current_score)
        else:
            self.game_scenes.next_level()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

                if self.current_level >= len(self.game_level_scenes):
                    self.display_player_score.current_score = 0
                    self.current_level = 1

                self.continue_screen = False
                self.game_current_level_scene = self.game_level_scenes[self.current_level]
                self.game_reset()
