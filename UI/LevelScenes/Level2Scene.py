import pygame

from UI.Levels import Levels


class LevelTwoScene(Levels):
    def __init__(self, level_score):
        super().__init__()
        self.level_score = level_score

    def display_level(self, screen):
        pygame.display.set_caption("Level 2")
        # Text
        self.level_text = self.game_font.render(
            "Level 2",
            True,
            'Black'
        ).convert_alpha()
        self.level_text_rect = self.level_text.get_rect(center=(800, 50))

        self.objective_text = self.game_font.render(
            f"- Kill 15 Ground Ravens",
            True,
            'Black').convert_alpha()
        self.objective_text_rect = self.objective_text.get_rect(center=(780, 100))

        self.progress_text = self.game_font.render(
            f"Ground Ravens Killed: {self.level_score}",
            True,
            'Black').convert_alpha()
        self.progress_text_rect = self.progress_text.get_rect(center=(800, 150))

        # Text BG
        bg = pygame.Surface((300, 100))  # the size of your rect
        bg.set_alpha(128)  # alpha level
        bg.fill('black')  # this fills the entire surface
        screen.blit(bg, (650, 30))  # (0,0) are the top-left coordinates

        # Draw
        screen.blit(self.level_text, self.level_text_rect)
        screen.blit(self.objective_text, self.objective_text_rect)
        screen.blit(self.progress_text, self.progress_text_rect)
