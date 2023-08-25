import pygame.sprite


class Levels(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.game_font = pygame.font.Font('Fonts/Amatic-Bold.ttf', 40)
        self.level_text = None
        self.objective_text = None
        self.objective_text_rect = None
        self.progress_text = None
        self.progress_text_rect = None
        self.level_text_rect = None

    def display_level(self, screen):
        pass

    def update(self, screen):
        self.display_level(screen)
