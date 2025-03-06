import pygame.sprite
from UI.health import Health


class EnemyHealth(Health):
    def __init__(self, current_health, max_health, pos_x, pos_y):
        super().__init__()

        self.width = 50
        self.height = 10
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = current_health
        self.max_health = max_health