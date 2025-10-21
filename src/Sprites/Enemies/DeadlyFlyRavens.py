from random import randint
import pygame
from src.Sprites.enemy import Enemy


class DeadlyFlyRaven(Enemy):
    def __init__(self):
        super().__init__()

        self.enemy_health = 100
        self.enemy_speed = 7.5
        self.sprites_speed = 0.4
        self.load_sprites()
        self.enemy_height_pos = randint(
            self.PLAYER_GROUND_POS - 40, self.PLAYER_GROUND_POS - 20
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
            pygame.image.load(
                f"assets/Deadly Raven Bird/DeadlyFlyRight{i}.png"
            ).convert_alpha()
            for i in range(1, 7)
        ]
        self.enemy_frames_left = [
            pygame.image.load(
                f"assets/Deadly Raven Bird/DeadlyFlyLeft{i}.png"
            ).convert_alpha()
            for i in range(1, 7)
        ]
