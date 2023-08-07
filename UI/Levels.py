import pygame.sprite


class Levels(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1000, 550
        self.game_screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.game_font = pygame.font.Font('Fonts/Amatic-Bold.ttf', 40)
        self.progress_text = None
        self.progress_text_rect = None

    def display_level(self):
        pass

    def update(self, screen):
        pass


class LevelOne(Levels):
    def __init__(self, level_score):
        super().__init__()
        self.level_score = level_score

    def display_level(self):
        pygame.display.set_caption("Level 1")
        # Text
        objective_text = self.game_font.render(
            f"Level 1: Kill 5 Ground Ravens",
            True,
            'Black').convert_alpha()
        objective_text_rect = objective_text.get_rect(center=(830, 70))

        # Draw
        self.game_screen.blit(objective_text, objective_text_rect)

    def update(self, screen):

        self.progress_text = self.game_font.render(
            f"Ground Ravens Killed: {self.level_score}",
            True,
            'Black').convert_alpha()
        self.progress_text_rect = self.progress_text.get_rect(center=(815, 120))

        screen.blit(self.progress_text, self.progress_text_rect)


class LevelTwo(Levels):
    def __init__(self, level_score):
        super().__init__()
        self.level_score = level_score

    def display_level(self):
        pygame.display.set_caption("Level 2")
        # Text
        objective_text = self.game_font.render(
            f"Level 2: Kill 15 Ground Ravens",
            True,
            'Black').convert_alpha()
        objective_text_rect = objective_text.get_rect(center=(830, 70))

        # Draw
        self.game_screen.blit(objective_text, objective_text_rect)

    def update(self, screen):

        self.progress_text = self.game_font.render(
            f"Ground Ravens Killed: {self.level_score}",
            True,
            'Black').convert_alpha()
        self.progress_text_rect = self.progress_text.get_rect(center=(815, 120))

        screen.blit(self.progress_text, self.progress_text_rect)
