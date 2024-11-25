import pygame

from UI.levels import Levels


class LevelFourScene(Levels):
    def __init__(self, level_score, fl_kills):
        super().__init__()

        self.level_score = level_score
        self.fl_kills = fl_kills

        self.objective2_text = None
        self.objective2_text_rect = None

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
            f"- Kill 5 Fly Ravens Without Taking Damage  {self.fl_kills}/5",
            True,
            'green' if self.fl_kills == 10 else 'black').convert_alpha()
        self.objective_text_rect = self.objective_text.get_rect(center=(730, 100))

        # Text BG
        bg = pygame.Surface((490, 105))  # the size of your rect
        bg.set_alpha(128)  # alpha level
        bg.fill('black')  # this fills the entire surface
        screen.blit(bg, (490, 30))  # (0,0) are the top-left coordinates

        # Draw
        screen.blit(self.level_text, self.level_text_rect)
        screen.blit(self.objective_text, self.objective_text_rect)
