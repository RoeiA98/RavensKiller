import pygame.sprite


class Levels(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.game_font = pygame.font.Font('Fonts/Amatic-Bold.ttf', 40)
        self.objective_text = None
        self.objective_text_rect = None
        self.progress_text = None
        self.progress_text_rect = None

    def display_level(self, screen):
        pass

    def update(self, screen):
        self.display_level(screen)


class LevelOne(Levels):
    def __init__(self, level_score):
        super().__init__()
        self.level_score = level_score

    def display_level(self, screen):
        pygame.display.set_caption("Level 1")
        # Text
        self.objective_text = self.game_font.render(
            f"Level 1: Kill 5 Ground Ravens",
            True,
            'Black').convert_alpha()
        self.objective_text_rect = self.objective_text.get_rect(center=(830, 70))

        self.progress_text = self.game_font.render(
            f"Ground Ravens Killed: {self.level_score}",
            True,
            'Black').convert_alpha()
        self.progress_text_rect = self.progress_text.get_rect(center=(815, 120))

        # Draw
        screen.blit(self.objective_text, self.objective_text_rect)
        screen.blit(self.progress_text, self.progress_text_rect)


class LevelTwo(Levels):
    def __init__(self, level_score):
        super().__init__()
        self.level_score = level_score

    def display_level(self, screen):
        pygame.display.set_caption("Level 2")
        # Text
        self.objective_text = self.game_font.render(
            f"Level 2: Kill 15 Ground Ravens",
            True,
            'Black').convert_alpha()
        self.objective_text_rect = self.objective_text.get_rect(center=(830, 70))

        self.progress_text = self.game_font.render(
            f"Ground Ravens Killed: {self.level_score}",
            True,
            'Black').convert_alpha()
        self.progress_text_rect = self.progress_text.get_rect(center=(815, 120))

        # Draw
        screen.blit(self.objective_text, self.objective_text_rect)
        screen.blit(self.progress_text, self.progress_text_rect)
