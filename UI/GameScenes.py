import pygame.sprite # type: ignore
from SpritesLogic.enemy import *


class GameScenes(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.continue_screen = None
        self.final_screen = None
        self.game_intro_status = None
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1000, 550
        self.game_screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.game_font = pygame.font.Font('Fonts/Amatic-Bold.ttf', 50)
        self.image = pygame.image.load('assets/gameBG3.png').convert()
        self.rect = None
        self.keys = pygame.key.get_pressed()

    def game_intro(self):

        pygame.display.set_caption("Welcome")
        pygame.display.update()
        
        welcome_text = self.game_font.render(
            f"Welcome to RavensKiller",
            True,
            'Black').convert_alpha()
        welcome_text_rect = welcome_text.get_rect(center=(500, 100))

        instructions_text = self.game_font.render(
            f"Use arrows to move around, SPACE to shoot and ESC to pause",
            True,
            'Black').convert_alpha()
        instructions_text_rect = welcome_text.get_rect(center=(280, 150))

        start_game_text = self.game_font.render(
            f"Press Enter to Start!",
            True,
            'Black').convert_alpha()
        start_game_text_rect = start_game_text.get_rect(center=(500, 230))

        
        self.game_screen.blit(self.image, (0, 0))
        self.game_screen.blit(welcome_text, welcome_text_rect)
        self.game_screen.blit(instructions_text, instructions_text_rect)
        self.game_screen.blit(start_game_text, start_game_text_rect)

    def game_active(self):
        pygame.display.set_caption("Ravens Killer")
        self.game_screen.blit(self.image, (0, 0))

    def next_level(self, current_level, num_of_levels):

        pygame.display.set_caption("Next Level")
        pygame.display.update()
        
        congrats_text = self.game_font.render(
            f"Great Job!",
            True,
            'Black').convert_alpha()
        congrats_text_rect = congrats_text.get_rect(center=(500, 200))

        if current_level == num_of_levels - 1:
            continue_text = self.game_font.render(
            f"Press Enter to play level the final level!",
            True,
            'Black'
        ).convert_alpha()
        else:
            continue_text = self.game_font.render(
            f"Press Enter to play level {current_level}!",
            True,
            'Black'
        ).convert_alpha()
        
        continue_text_rect = continue_text.get_rect(center=(500, 250))

        self.game_screen.blit(self.image, (0, 0))
        self.game_screen.blit(congrats_text, congrats_text_rect)
        self.game_screen.blit(continue_text, continue_text_rect)

    def pause_screen(self):

        pygame.display.set_caption("Pause")
        pygame.display.update()

        congrats_text = self.game_font.render(
            f"GAME PAUSED!",
            True,
            'Black').convert_alpha()
        congrats_text_rect = congrats_text.get_rect(center=(500, 200))

        continue_text = self.game_font.render(
            f"Press ESC to continue",
            True,
            'Black').convert_alpha()
        continue_text_rect = continue_text.get_rect(center=(500, 250))

        self.game_screen.blit(self.image, (0, 0))
        self.game_screen.blit(congrats_text, congrats_text_rect)
        self.game_screen.blit(continue_text, continue_text_rect)

    def game_over_scene(self, final_score):

        pygame.display.set_caption("Game Over")

        gameover_text = self.game_font.render(
            f"GAME OVER!",
            True,
            'Black').convert_alpha()
        gameover_text_rect = gameover_text.get_rect(center=(500, 100))

        gameover_score = self.game_font.render(
            f"Final score: {final_score}",
            True,
            'Black').convert_alpha()
        gameover_score_rect = gameover_score.get_rect(center=(500, 150))

        restart_text = self.game_font.render(
            f"Press Enter to try again",
            True,
            'Black').convert_alpha()
        restart_text_rect = gameover_text.get_rect(center=(430, 200))

        self.game_screen.blit(self.image, (0, 0))
        self.game_screen.blit(gameover_text, gameover_text_rect)
        self.game_screen.blit(gameover_score, gameover_score_rect)
        self.game_screen.blit(restart_text, restart_text_rect)

    def final_scene(self, final_score):

        pygame.display.set_caption("Final")
        pygame.display.update()

        congrats_text = self.game_font.render(
            f"Congratulations, you beat the game!",
            True,
            'Black').convert_alpha()
        congrats_text_rect = congrats_text.get_rect(center=(500, 100))

        continue_text = self.game_font.render(
            f"Your final score: {final_score}",
            True,
            'Black').convert_alpha()
        continue_text_rect = continue_text.get_rect(center=(500, 150))

        restart_text = self.game_font.render(
            f"Press Enter to Restart!",
            True,
            'Black').convert_alpha()
        restart_text_rect = restart_text.get_rect(center=(500, 250))

        self.game_screen.blit(self.image, (0, 0))
        self.game_screen.blit(congrats_text, congrats_text_rect)
        self.game_screen.blit(continue_text, continue_text_rect)
        self.game_screen.blit(restart_text, restart_text_rect)
