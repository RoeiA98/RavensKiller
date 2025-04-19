from random import randint
import pygame
from src.Sprites.enemy import Enemy


class FlyRaven(Enemy):
    def __init__(self):
        super().__init__()

        self.enemy_health = 100
        self.enemy_speed = 6
        self.sprites_speed = 0.1
        self.load_sprites()
        self.enemy_height_pos = randint(
            self.PLAYER_GROUND_POS - 200, self.PLAYER_GROUND_POS - 150
        )

        self.enemy_spawn_coordinates(self.enemy_direction)

        self.image = self.enemy_frames[self.enemy_animation_index]
        self.rect = self.image.get_rect(
            midbottom=(self.enemy_width_pos, self.enemy_height_pos)
        )

    def enemy_sprite_speed(self):
        self.enemy_animation_index += self.sprites_speed
        if self.enemy_animation_index >= len(self.enemy_frames):
            self.enemy_animation_index = 0
        self.image = self.enemy_frames[int(self.enemy_animation_index)]

    def load_sprites(self):
        self.enemy_frames_right = [
            pygame.image.load(f"assets/Raven Bird/FlyRight{i}.png").convert_alpha()
            for i in range(1, 7)
        ]
        self.enemy_frames_left = [
            pygame.image.load(f"assets/Raven Bird/FlyLeft{i}.png").convert_alpha()
            for i in range(1, 7)
        ]
