import pygame
from Sprites.Enemy import Enemy
from UI.Health import EnemyHealth


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
