import pygame


class FPS:
    
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Verdana", 20)
        self.text = self.font.render(str(self.clock.get_fps()), True, 'black')

    def render(self, display):
        self.text = self.font.render("FPS: " + str(round(self.clock.get_fps(), 2)), True, 'black')
        display.blit(self.text, (0, 0))
