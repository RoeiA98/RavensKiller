import pygame # type: ignore
from src.Game.setup import *
from utils.utils import set_spawn_rate

class Level4(Game):

    def __init__(self):
        super().__init__()

    def play(self):
        """
        Level logic:
            Objective:  - Kill 5 fly ravens without taking damage

        """

        """Level settings:"""
        self.collisions.fly_raven_damage = 100

        self.spawns.deadly_raven_spawn = 0
        self.spawns.ground_raven_spawn = 0
        self.spawns.fly_raven_spawn = set_spawn_rate(1000, 2000)

        self.events_handler()

        """Level display:"""
        self.game_active()

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1
            self.fly_ravens_kills += 1

        if self.fly_ravens_kills == 5:
            self.stop_level()
        
        
    def display_level(self, screen):
        pygame.display.set_caption("Level 4")
        # Text
        self.level_text = self.game_font.render(
            "Level 4",
            True,
            'Black'
        ).convert_alpha()
        self.level_text_rect = self.level_text.get_rect(center=(750, 50))

        # Objectives
        self.objective_text = self.game_font.render(
            f"- Kill 5 Fly Ravens Without Taking Damage  {self.fly_ravens_kills}/5",
            True,
            'green' if self.fly_ravens_kills == 10 else 'black').convert_alpha()
        self.objective_text_rect = self.objective_text.get_rect(center=(730, 100))

        # Text BG
        bg = pygame.Surface((490, 105))  # the size of your rect
        bg.set_alpha(128)  # alpha level
        bg.fill('black')  # this fills the entire surface
        screen.blit(bg, (490, 30))  # (0,0) are the top-left coordinates

        # Draw
        screen.blit(self.level_text, self.level_text_rect)
        screen.blit(self.objective_text, self.objective_text_rect)
