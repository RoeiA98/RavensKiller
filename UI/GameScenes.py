import pygame.sprite
from Sprites.Enemies import *


class GameScenes(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.continue_screen = None
        self.game_intro_status = None
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1000, 550
        self.game_screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.game_font = pygame.font.Font('Fonts/Amatic-Bold.ttf', 50)
        self.image = pygame.image.load('Graphics/gameBG3.png').convert()
        self.rect = None
        self.keys = pygame.key.get_pressed()

    def game_intro(self):

        self.game_intro_status = True
        while self.game_intro_status:
            pygame.display.update()
            pygame.display.set_caption("Welcome")
            # Text
            welcome_text = self.game_font.render(
                f"Welcome to RavensKiller",
                True,
                'Black').convert_alpha()
            welcome_text_rect = welcome_text.get_rect(center=(500, 200))

            start_game_text = self.game_font.render(
                f"Press Space to Start!",
                True,
                'Black').convert_alpha()
            start_game_text_rect = start_game_text.get_rect(center=(500, 250))

            # Draw
            self.game_screen.blit(self.image, (0, 0))
            self.game_screen.blit(welcome_text, welcome_text_rect)
            self.game_screen.blit(start_game_text, start_game_text_rect)

            for intro_event in pygame.event.get():
                if intro_event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if intro_event.type == pygame.KEYDOWN and intro_event.key == pygame.K_SPACE:
                    self.game_intro_status = False

        return True

    def game_active(self):
        pygame.display.set_caption("Ravens Killer")
        self.game_screen.blit(self.image, (0, 0))

    def next_level(self):

        self.continue_screen = True
        pygame.display.set_caption("Next Level")

        while self.continue_screen:
            pygame.display.update()
            # Text
            congrats_text = self.game_font.render(
                f"Great Job!",
                True,
                'Black').convert_alpha()
            congrats_text_rect = congrats_text.get_rect(center=(500, 200))

            continue_text = self.game_font.render(
                f"Press Space for the Next Level!",
                True,
                'Black').convert_alpha()
            continue_text_rect = continue_text.get_rect(center=(500, 250))

            # Draw
            self.game_screen.blit(self.image, (0, 0))
            self.game_screen.blit(congrats_text, congrats_text_rect)
            self.game_screen.blit(continue_text, continue_text_rect)

            for intro_event in pygame.event.get():
                if intro_event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if intro_event.type == pygame.KEYDOWN and intro_event.key == pygame.K_SPACE:
                    self.continue_screen = False

        return True

    def game_over(self, final_score):

        pygame.display.set_caption("Game Over")
        # Text
        gameover_text = self.game_font.render(
            f"GAME OVER!",
            True,
            'Black').convert_alpha()
        gameover_text_rect = gameover_text.get_rect(center=(500, 100))

        gameover_score = self.game_font.render(
            f"Final score: {final_score}",
            True,
            'Black').convert_alpha()
        gameover_score_rect = gameover_score.get_rect(center=(500, 450))

        restart_text = self.game_font.render(
            f"Press Space to try again",
            True,
            'Black').convert_alpha()
        restart_text_rect = gameover_text.get_rect(center=(430, 500))

        # Draw
        self.game_screen.blit(self.image, (0, 0))
        self.game_screen.blit(gameover_text, gameover_text_rect)
        self.game_screen.blit(gameover_score, gameover_score_rect)
        self.game_screen.blit(restart_text, restart_text_rect)
