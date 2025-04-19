import pygame.sprite
from UI.health import Health


class PlayerHealth(Health):
    def __init__(self):
        super().__init__()

        self.width = 100
        self.height = 40
        self.pos_x = 50
        self.pos_y = 100
        self.hp = 100  # default starting health
        self.max_health = 100
        self.hp_text = None
        self.hp_text_rect = None

    def draw_hp_text(self, screen):
        self.hp_text = self.font.render(f"{self.hp}", True, "Black").convert_alpha()
        self.hp_text_rect = self.hp_text.get_rect(center=(100, 118))
        screen.blit(self.hp_text, self.hp_text_rect)
