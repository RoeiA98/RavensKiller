import pygame # type: ignore

from UI.levels import Levels


class Scene(Levels):
    def __init__(self, level_score, gr_kills, fl_kills):
        super().__init__()

        self.level_score = level_score
        self.gr_kills = gr_kills
        self.fl_kills = fl_kills

        self.objective2_text = None
        self.objective2_text_rect = None

    def display_level(self, screen):
        pygame.display.set_caption("Level 3")
        # Text
        self.level_text = self.game_font.render(
            "Level 3",
            True,
            'Black'
        ).convert_alpha()
        self.level_text_rect = self.level_text.get_rect(center=(800, 50))

        # Objectives
        self.objective_text = self.game_font.render(
            f"- Kill 10 Ground Ravens   {self.gr_kills}/10",
            True,
            'green' if self.gr_kills == 10 else 'black').convert_alpha()
        self.objective_text_rect = self.objective_text.get_rect(center=(780, 100))

        self.objective2_text = self.game_font.render(
            f"- Kill 3 Fly Ravens                 {self.fl_kills}/3",
            True,
            'green' if self.fl_kills == 3 else 'black').convert_alpha()
        self.objective2_text_rect = self.objective_text.get_rect(center=(780, 140))

        # Text BG
        bg = pygame.Surface((330, 140))  # the size of your rect
        bg.set_alpha(128)  # alpha level
        bg.fill('black')  # this fills the entire surface
        screen.blit(bg, (620, 30))  # (0,0) are the top-left coordinates

        # Draw
        screen.blit(self.level_text, self.level_text_rect)
        screen.blit(self.objective_text, self.objective_text_rect)
        screen.blit(self.objective2_text, self.objective2_text_rect)
