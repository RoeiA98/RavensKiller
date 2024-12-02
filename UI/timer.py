import pygame # type: ignore

class Timer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.font = pygame.font.SysFont("Verdana", 25)

    def display_timer(self, screen, elapsed_time):
        timer_text = self.font.render(f"Time: {str(elapsed_time)[:-4]}", True, "White")
        screen.blit(timer_text, (750, 515))
