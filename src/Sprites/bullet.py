import pygame.sprite


class Bullet(pygame.sprite.Sprite):
    def __init__(self, player_x, player_y, player_direction):
        super().__init__()

        self.player_direction = player_direction
        self.image = pygame.image.load("assets/Player/bullet2.png")
        self.rect = self.image.get_rect(center=(player_x, player_y))
        self.bullet_speed = 17

    def update(self):
        if self.player_direction:
            self.rect.x -= self.bullet_speed
        else:
            self.rect.x += self.bullet_speed

        # deleting bullets outside of screen
        if self.rect.x >= 1000 or self.rect.x <= 0:
            self.kill()
