import pygame.sprite # type: ignore

class Health(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.width = None
        self.height = None
        self.pos_x = None
        self.pos_y = None
        self.hp = None
        self.max_health = None
        self.ratio = 0
        self.font = pygame.font.Font('Fonts/Amatic-Bold.ttf', 40)

    def draw(self, screen):
        self.ratio = self.hp / self.max_health
        pygame.draw.rect(screen, "red", (self.pos_x, self.pos_y, self.width, self.height))
        pygame.draw.rect(screen, "green", (self.pos_x, self.pos_y, self.width * self.ratio, self.height))


class PlayerHealth(Health):
    def __init__(self, current_health, max_health):
        super().__init__()

        self.width = 100
        self.height = 40
        self.pos_x = 50
        self.pos_y = 100
        self.hp = current_health
        self.max_health = max_health
        self.hp_text = None
        self.hp_text_rect = None

    def draw_hp_text(self, screen):
        self.hp_text = self.font.render(f"{self.hp}", True, 'Black').convert_alpha()
        self.hp_text_rect = self.hp_text.get_rect(center=(100, 118))
        screen.blit(self.hp_text, self.hp_text_rect)


class EnemyHealth(Health):
    def __init__(self, current_health, max_health, pos_x, pos_y):
        super().__init__()

        self.width = 50
        self.height = 10
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.hp = current_health
        self.max_health = max_health
