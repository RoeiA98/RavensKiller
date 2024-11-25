import pygame # type: ignore
from SpritesLogic.enemy import Enemy
from UI.health import EnemyHealth


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

        self.enemy_frames_right = [
            pygame.image.load('assets/Raven/RunRight1.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunRight2.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunRight3.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunRight4.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunRight5.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunRight6.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunRight7.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunRight8.png').convert_alpha()
        ]

        self.enemy_frames_left = [
            pygame.image.load('assets/Raven/RunLeft1.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunLeft2.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunLeft3.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunLeft4.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunLeft5.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunLeft6.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunLeft7.png').convert_alpha(),
            pygame.image.load('assets/Raven/RunLeft8.png').convert_alpha() 
        ]

    def draw_health(self):
        if self.enemy_direction:    # right direction
            self.health_settings = EnemyHealth(self.health, self.starting_health, self.rect.x + 35, self.rect.y - 15)
        else:                       # left direction
            self.health_settings = EnemyHealth(self.health, self.starting_health, self.rect.x, self.rect.y - 15)
        self.health_settings.draw(self.screen)
