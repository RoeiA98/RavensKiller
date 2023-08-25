from random import randint
import pygame.sprite
from UI.Health import *


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
            self.enemy_width_pos = randint(-500, -100)
            self.enemy_frames = self.enemy_frames_right
        else:
            self.enemy_width_pos = randint(1100, 1300)
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


class FlyRaven(Enemy):
    def __init__(self):
        super().__init__()

        self.enemy_health = 100
        self.enemy_speed = 6
        self.sprites_speed = 0.1
        self.load_sprites()
        self.enemy_height_pos = randint(self.PLAYER_GROUND_POS-200, self.PLAYER_GROUND_POS-150)

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
        fly_raven_right1 = pygame.image.load('Graphics/Raven Bird/FlyRight1.png').convert_alpha()
        fly_raven_right2 = pygame.image.load('Graphics/Raven Bird/FlyRight2.png').convert_alpha()
        fly_raven_right3 = pygame.image.load('Graphics/Raven Bird/FlyRight3.png').convert_alpha()
        fly_raven_right4 = pygame.image.load('Graphics/Raven Bird/FlyRight4.png').convert_alpha()
        fly_raven_right5 = pygame.image.load('Graphics/Raven Bird/FlyRight5.png').convert_alpha()
        fly_raven_right6 = pygame.image.load('Graphics/Raven Bird/FlyRight6.png').convert_alpha()
        self.enemy_frames_right = [fly_raven_right1,
                                   fly_raven_right2,
                                   fly_raven_right3,
                                   fly_raven_right4,
                                   fly_raven_right5,
                                   fly_raven_right6]

        # fly raven animation left
        fly_raven_left1 = pygame.image.load('Graphics/Raven Bird/FlyLeft1.png').convert_alpha()
        fly_raven_left2 = pygame.image.load('Graphics/Raven Bird/FlyLeft2.png').convert_alpha()
        fly_raven_left3 = pygame.image.load('Graphics/Raven Bird/FlyLeft3.png').convert_alpha()
        fly_raven_left4 = pygame.image.load('Graphics/Raven Bird/FlyLeft4.png').convert_alpha()
        fly_raven_left5 = pygame.image.load('Graphics/Raven Bird/FlyLeft5.png').convert_alpha()
        fly_raven_left6 = pygame.image.load('Graphics/Raven Bird/FlyLeft6.png').convert_alpha()
        self.enemy_frames_left = [fly_raven_left1,
                                  fly_raven_left2,
                                  fly_raven_left3,
                                  fly_raven_left4,
                                  fly_raven_left5,
                                  fly_raven_left6]


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


class GroundRaven(Enemy):
    def __init__(self, health, screen):
        super().__init__()

        self.screen = screen
        self.health = health
        self.starting_health = health
        self.enemy_speed = 3
        self.sprites_speed = 0.2
        self.load_sprites()
        self.enemy_height_pos = self.PLAYER_GROUND_POS
        self.health_settings = None

        self.enemy_spawn_coordinates(self.enemy_direction)

        self.image = self.enemy_frames[self.enemy_animation_index]
        self.rect = self.image.get_rect(midbottom=(self.enemy_width_pos, self.enemy_height_pos))

    def enemy_sprite_speed(self):
        self.enemy_animation_index += self.sprites_speed
        if self.enemy_animation_index >= len(self.enemy_frames):
            self.enemy_animation_index = 0
        self.image = self.enemy_frames[int(self.enemy_animation_index)]

    def load_sprites(self):
        # ground raven animation right
        ground_raven_right1 = pygame.image.load('Graphics/Raven/RunRight1.png').convert_alpha()
        ground_raven_right2 = pygame.image.load('Graphics/Raven/RunRight2.png').convert_alpha()
        ground_raven_right3 = pygame.image.load('Graphics/Raven/RunRight3.png').convert_alpha()
        ground_raven_right4 = pygame.image.load('Graphics/Raven/RunRight4.png').convert_alpha()
        ground_raven_right5 = pygame.image.load('Graphics/Raven/RunRight5.png').convert_alpha()
        ground_raven_right6 = pygame.image.load('Graphics/Raven/RunRight6.png').convert_alpha()
        ground_raven_right7 = pygame.image.load('Graphics/Raven/RunRight7.png').convert_alpha()
        ground_raven_right8 = pygame.image.load('Graphics/Raven/RunRight8.png').convert_alpha()
        self.enemy_frames_right = [ground_raven_right1,
                                   ground_raven_right2,
                                   ground_raven_right3,
                                   ground_raven_right4,
                                   ground_raven_right5,
                                   ground_raven_right6,
                                   ground_raven_right7,
                                   ground_raven_right8]

        # ground raven animation left
        ground_raven_left1 = pygame.image.load('Graphics/Raven/RunLeft1.png').convert_alpha()
        ground_raven_left2 = pygame.image.load('Graphics/Raven/RunLeft2.png').convert_alpha()
        ground_raven_left3 = pygame.image.load('Graphics/Raven/RunLeft3.png').convert_alpha()
        ground_raven_left4 = pygame.image.load('Graphics/Raven/RunLeft4.png').convert_alpha()
        ground_raven_left5 = pygame.image.load('Graphics/Raven/RunLeft5.png').convert_alpha()
        ground_raven_left6 = pygame.image.load('Graphics/Raven/RunLeft6.png').convert_alpha()
        ground_raven_left7 = pygame.image.load('Graphics/Raven/RunLeft7.png').convert_alpha()
        ground_raven_left8 = pygame.image.load('Graphics/Raven/RunLeft8.png').convert_alpha()
        self.enemy_frames_left = [ground_raven_left1,
                                  ground_raven_left2,
                                  ground_raven_left3,
                                  ground_raven_left4,
                                  ground_raven_left5,
                                  ground_raven_left6,
                                  ground_raven_left7,
                                  ground_raven_left8]

    def draw_health(self):
        if self.enemy_direction:    # right direction
            self.health_settings = EnemyHealth(self.health, self.starting_health, self.rect.x + 35, self.rect.y - 15)
        else:                       # left direction
            self.health_settings = EnemyHealth(self.health, self.starting_health, self.rect.x, self.rect.y - 15)
        self.health_settings.draw(self.screen)
