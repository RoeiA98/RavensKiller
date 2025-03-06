import pygame.sprite

class Health(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = None
        self.height = None
        self.pos_x = None
        self.pos_y = None
        self.hp = None
        self.max_health = None
        self.font = pygame.font.Font('fonts/Amatic-Bold.ttf', 40)

    def draw(self, screen):
        ratio = self.hp / self.max_health
        pygame.draw.rect(screen, "red", (self.pos_x, self.pos_y, self.width, self.height))
        pygame.draw.rect(screen, "green", (self.pos_x, self.pos_y, self.width * ratio, self.height))
