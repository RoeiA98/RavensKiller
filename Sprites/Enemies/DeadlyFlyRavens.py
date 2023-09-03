from random import randint
import pygame
from Sprites.Enemy import Enemy


class DeadlyFlyRaven(Enemy):
    def __init__(self):
        super().__init__()

        self.enemy_health = 100
        self.enemy_speed = 7.5
        self.sprites_speed = 0.4
        self.load_sprites()
        self.enemy_height_pos = randint(self.PLAYER_GROUND_POS-40, self.PLAYER_GROUND_POS-20)

        self.enemy_spawn_coordinates(self.enemy_direction)

        self.image = self.enemy_frames[self.enemy_animation_index]
        self.rect = self.image.get_rect(midbottom=(self.enemy_width_pos, self.enemy_height_pos))

    def enemy_sprite_speed(self):
        self.enemy_animation_index += self.sprites_speed
        if self.enemy_animation_index >= len(self.enemy_frames):
            self.enemy_animation_index = 0
        self.image = self.enemy_frames[int(self.enemy_animation_index)]

    def load_sprites(self):
        # fly raven animation right
        fly_raven_right1 = pygame.image.load('Graphics/Deadly Raven Bird/DeadlyFlyRight1.png').convert_alpha()
        fly_raven_right2 = pygame.image.load('Graphics/Deadly Raven Bird/DeadlyFlyRight2.png').convert_alpha()
        fly_raven_right3 = pygame.image.load('Graphics/Deadly Raven Bird/DeadlyFlyRight3.png').convert_alpha()
        fly_raven_right4 = pygame.image.load('Graphics/Deadly Raven Bird/DeadlyFlyRight4.png').convert_alpha()
        fly_raven_right5 = pygame.image.load('Graphics/Deadly Raven Bird/DeadlyFlyRight5.png').convert_alpha()
        fly_raven_right6 = pygame.image.load('Graphics/Deadly Raven Bird/DeadlyFlyRight6.png').convert_alpha()
        self.enemy_frames_right = [fly_raven_right1,
                                   fly_raven_right2,
                                   fly_raven_right3,
                                   fly_raven_right4,
                                   fly_raven_right5,
                                   fly_raven_right6]

        # fly raven animation left
        fly_raven_left1 = pygame.image.load('Graphics/Deadly Raven Bird/DeadlyFlyLeft1.png').convert_alpha()
        fly_raven_left2 = pygame.image.load('Graphics/Deadly Raven Bird/DeadlyFlyLeft2.png').convert_alpha()
        fly_raven_left3 = pygame.image.load('Graphics/Deadly Raven Bird/DeadlyFlyLeft3.png').convert_alpha()
        fly_raven_left4 = pygame.image.load('Graphics/Deadly Raven Bird/DeadlyFlyLeft4.png').convert_alpha()
        fly_raven_left5 = pygame.image.load('Graphics/Deadly Raven Bird/DeadlyFlyLeft5.png').convert_alpha()
        fly_raven_left6 = pygame.image.load('Graphics/Deadly Raven Bird/DeadlyFlyLeft6.png').convert_alpha()
        self.enemy_frames_left = [fly_raven_left1,
                                  fly_raven_left2,
                                  fly_raven_left3,
                                  fly_raven_left4,
                                  fly_raven_left5,
                                  fly_raven_left6]
