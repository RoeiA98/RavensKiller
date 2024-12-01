import pygame.sprite # type: ignore
from src.SpritesLogic.bullet import *
from UI.health import *


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
        self.image = pygame.image.load('assets/Player/PlayerIdleRight.png').convert_alpha()
        self.idle_right = pygame.image.load('assets/Player/PlayerIdleRight.png').convert_alpha()
        self.idle_left = pygame.image.load('assets/Player/PlayerIdleLeft.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=(500, self.PLAYER_GROUND_POS))

    def player_reset_pos(self):
        self.rect = self.image.get_rect(midbottom=(500, self.PLAYER_GROUND_POS))
        self.gravity = 0
        if self.player_current_direction:
            self.image = self.idle_left
        else:
            self.image = self.idle_right
    
    def player_shoot_bullet(self, player_x, player_y, direction):
        if direction:
            return Bullet(player_x, player_y+15, direction)
        return Bullet(player_x+50, player_y+15, direction)

    def player_load_sprites(self):
        # player running sprites
        self.player_run_right = [pygame.image.load(f'assets/Player/RunRightF{i}.png') for i in range(1, 9)]
        self.player_run_left = [pygame.image.load(f'assets/Player/RunLeftF{i}.png') for i in range(1, 9)]

        # player shooting sprites
        self.player_shoot_right = [pygame.image.load(f'assets/Player/ShootRight{i}.png') for i in range(1, 7)]
        self.player_shoot_left = [pygame.image.load(f'assets/Player/ShootLeft{i}.png') for i in range(1, 7)]

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
