from random import randint
from UI.health_bar import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.PLAYER_GROUND_POS = 470
        self.enemy_frames_left = None
        self.enemy_frames_right = None
        self.enemy_frames = []
        self.enemy_speed = 0
        self.enemy_health = None
        self.enemy_width_pos = 0
        # direction: 1 = right, 0 = left
        self.enemy_direction = randint(0, 1)
        self.enemy_animation_index = 0
        self.image = None
        self.rect = None

    def enemy_spawn_coordinates(self, direction):
        if direction:
            self.enemy_width_pos = randint(-500, -400)
            self.enemy_frames = self.enemy_frames_right
        else:
            self.enemy_width_pos = randint(1200, 1300)
            self.enemy_frames = self.enemy_frames_left

    def enemy_sprite_speed(self):
        pass

    def draw_health(self):
        pass

    def update(self):
        self.enemy_sprite_speed()
        if self.enemy_direction:
            self.rect.x += self.enemy_speed
        else:
            self.rect.x -= self.enemy_speed
        self.draw_health()
        self.remove_enemy()

    def remove_enemy(self):
        if self.rect.x > 1400 or self.rect.x < -500:
            self.kill()
