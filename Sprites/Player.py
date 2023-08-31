import pygame.sprite
from Sprites.Bullet import *
from UI.Health import *


def shoot_bullet(player_x, player_y, direction):
    if direction:
        return Bullet(player_x, player_y+15, direction)
    return Bullet(player_x+50, player_y+15, direction)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        # General
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 550
        self.PLAYER_GROUND_POS = 470

        # Player Attributes
        self.player_index = 0
        self.player_shoot_index = 0
        self.gravity = 0
        self.player_speed = 3
        self.shooting_speed = 0.5
        self.player_damage = 50
        self.player_current_direction = 0  # 0 = right, 1 = left
        self.player_run_right = None
        self.player_run_left = None
        self.player_shoot_right = None
        self.player_shoot_left = None

        # Sprites
        self.player_load_sprites()
        self.image = pygame.image.load('Graphics/Player/PlayerIdleRight.png').convert_alpha()
        self.idle_right = pygame.image.load('Graphics/Player/PlayerIdleRight.png').convert_alpha()
        self.idle_left = pygame.image.load('Graphics/Player/PlayerIdleLeft.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(500, self.PLAYER_GROUND_POS))

    def player_reset_pos(self):
        self.rect = self.image.get_rect(midbottom=(500, self.PLAYER_GROUND_POS))
        self.gravity = 0
        if self.player_current_direction:
            self.image = self.idle_left
        else:
            self.image = self.idle_right

    def player_load_sprites(self):
        # player running sprites
        # animation right
        player_run1_right = pygame.image.load('Graphics/Player/RunRightF1.png')
        player_run2_right = pygame.image.load('Graphics/Player/RunRightF2.png')
        player_run3_right = pygame.image.load('Graphics/Player/RunRightF3.png')
        player_run4_right = pygame.image.load('Graphics/Player/RunRightF4.png')
        player_run5_right = pygame.image.load('Graphics/Player/RunRightF5.png')
        player_run6_right = pygame.image.load('Graphics/Player/RunRightF6.png')
        player_run7_right = pygame.image.load('Graphics/Player/RunRightF7.png')
        player_run8_right = pygame.image.load('Graphics/Player/RunRightF8.png')
        self.player_run_right = [player_run1_right,
                                 player_run2_right,
                                 player_run3_right,
                                 player_run4_right,
                                 player_run5_right,
                                 player_run6_right,
                                 player_run7_right,
                                 player_run8_right]

        # animation left
        player_run1_left = pygame.image.load('Graphics/Player/RunLeftF1.png')
        player_run2_left = pygame.image.load('Graphics/Player/RunLeftF2.png')
        player_run3_left = pygame.image.load('Graphics/Player/RunLeftF3.png')
        player_run4_left = pygame.image.load('Graphics/Player/RunLeftF4.png')
        player_run5_left = pygame.image.load('Graphics/Player/RunLeftF5.png')
        player_run6_left = pygame.image.load('Graphics/Player/RunLeftF6.png')
        player_run7_left = pygame.image.load('Graphics/Player/RunLeftF7.png')
        player_run8_left = pygame.image.load('Graphics/Player/RunLeftF8.png')
        self.player_run_left = [player_run1_left,
                                player_run2_left,
                                player_run3_left,
                                player_run4_left,
                                player_run5_left,
                                player_run6_left,
                                player_run7_left,
                                player_run8_left]

        # player shooting sprites
        # animation right
        player_shoot1_right = pygame.image.load('Graphics/Player/ShootRight1.png')
        player_shoot2_right = pygame.image.load('Graphics/Player/ShootRight2.png')
        player_shoot3_right = pygame.image.load('Graphics/Player/ShootRight3.png')
        player_shoot4_right = pygame.image.load('Graphics/Player/ShootRight4.png')
        player_shoot5_right = pygame.image.load('Graphics/Player/ShootRight5.png')
        player_shoot6_right = pygame.image.load('Graphics/Player/ShootRight6.png')
        self.player_shoot_right = [player_shoot1_right,
                                   player_shoot2_right,
                                   player_shoot3_right,
                                   player_shoot4_right,
                                   player_shoot5_right,
                                   player_shoot6_right]

        # animation left
        player_shoot1_left = pygame.image.load('Graphics/Player/ShootLeft1.png')
        player_shoot2_left = pygame.image.load('Graphics/Player/ShootLeft2.png')
        player_shoot3_left = pygame.image.load('Graphics/Player/ShootLeft3.png')
        player_shoot4_left = pygame.image.load('Graphics/Player/ShootLeft4.png')
        player_shoot5_left = pygame.image.load('Graphics/Player/ShootLeft5.png')
        player_shoot6_left = pygame.image.load('Graphics/Player/ShootLeft6.png')
        self.player_shoot_left = [player_shoot1_left,
                                  player_shoot2_left,
                                  player_shoot3_left,
                                  player_shoot4_left,
                                  player_shoot5_left,
                                  player_shoot6_left]

    def player_running_animation(self):
        keys = pygame.key.get_pressed()

        if not keys[pygame.K_SPACE]:
            if keys[pygame.K_RIGHT]:
                self.player_index += 0.2
                self.player_current_direction = 0
                if self.player_index >= len(self.player_run_right):
                    self.player_index = 0
                if self.rect.right <= self.SCREEN_WIDTH:
                    self.rect.right += self.player_speed
                self.image = self.player_run_right[int(self.player_index)]
            elif keys[pygame.K_LEFT]:
                self.player_index += 0.2
                self.player_current_direction = 1
                if self.player_index >= len(self.player_run_left):
                    self.player_index = 0
                if self.rect.left >= 0:
                    self.rect.left -= self.player_speed
                self.image = self.player_run_left[int(self.player_index)]
            else:
                if self.player_current_direction:
                    self.image = self.idle_left
                else:
                    self.image = self.idle_right
                self.player_index = 0

    def player_jump(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.bottom == self.PLAYER_GROUND_POS:
            self.gravity = -20

    def player_shoot(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.player_current_direction == 0:
            self.player_shoot_index += self.shooting_speed
            if self.player_shoot_index >= len(self.player_shoot_right):
                self.player_shoot_index = len(self.player_shoot_right) - 1
            self.image = self.player_shoot_right[int(self.player_shoot_index)]
        elif keys[pygame.K_SPACE] and self.player_current_direction == 1:
            self.player_shoot_index += self.shooting_speed
            if self.player_shoot_index >= len(self.player_shoot_left):
                self.player_shoot_index = len(self.player_shoot_right) - 1
            self.image = self.player_shoot_left[int(self.player_shoot_index)]
        else:
            self.player_shoot_index = 0

    def player_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= self.PLAYER_GROUND_POS:
            self.rect.bottom = self.PLAYER_GROUND_POS

    def update(self):
        self.player_running_animation()
        self.player_jump()
        self.player_gravity()
        self.player_shoot()
