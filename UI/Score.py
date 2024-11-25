import pygame # type: ignore

class Score(pygame.sprite.Sprite):
    def __init__(self, starting_score):
        super().__init__()

        self.current_score = starting_score
        self.font = pygame.font.Font('Fonts/Amatic-Bold.ttf', 50)
        self.score_text = None
        self.score_text_rect = None

    def update(self, screen):
        self.score_text = self.font.render(f"Score: {self.current_score}", True, 'Black').convert_alpha()
        self.score_text_rect = self.score_text.get_rect(topleft=(50, 30))
        screen.blit(self.score_text, self.score_text_rect)
