import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.current_score = 0
        self.font = pygame.font.Font("fonts/Amatic-Bold.ttf", 50)
        self.score_text = None
        self.score_text_rect = None
        self.ground_ravens_kills = 0
        self.fly_ravens_kills = 0

    def update(self, screen):
        self.score_text = self.font.render(
            f"Score: {self.current_score}", True, "Black"
        ).convert_alpha()
        self.score_text_rect = self.score_text.get_rect(topleft=(50, 30))
        screen.blit(self.score_text, self.score_text_rect)
