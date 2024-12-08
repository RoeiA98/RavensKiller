import pygame  # type: ignore
from src.SpritesLogic.enemy import *

class GameScenes(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.continue_screen = None
        self.final_screen = None
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1000, 550
        self.game_screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.game_font = pygame.font.Font('fonts/Amatic-Bold.ttf', 50)
        self.image = pygame.image.load('assets/gameBG3.png').convert()
        self.rect = None
        self.keys = pygame.key.get_pressed()
        self.start_button_rect = pygame.Rect(400, 270, 200, 65)
        self.leaderboard_button_rect = pygame.Rect(400, 360, 200, 65)
        self.quit_button_rect = pygame.Rect(400, 450, 200, 65)
        self.return_to_menu_rect = pygame.Rect(400, 360, 200, 65)
        self.pause_quit_rect = pygame.Rect(400, 450, 200, 65)
        self.name_input = ""

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
            f"Press Enter to play the final level!",
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

        game_pause_text = self.game_font.render(
            f"GAME PAUSED!",
            True,
            'Black').convert_alpha()
        game_pause_text_rect = game_pause_text.get_rect(center=(500, 200))

        continue_text = self.game_font.render(
            f"Press ESC to continue",
            True,
            'Black').convert_alpha()
        continue_text_rect = continue_text.get_rect(center=(500, 250))
        
        return_to_menu_text = self.game_font.render(
            "Return To Menu",
            True,
            'Black').convert_alpha()
        return_to_menu_text_rect = return_to_menu_text.get_rect(center=self.return_to_menu_rect.center)
        
        quit_menu_text = self.game_font.render(
            "Quit",
            True,
            'Black').convert_alpha()
        quit_menu_text_rect = quit_menu_text.get_rect(center=self.pause_quit_rect.center)

        self.game_screen.blit(self.image, (0, 0))
        self.game_screen.blit(game_pause_text, game_pause_text_rect)
        self.game_screen.blit(continue_text, continue_text_rect)
        # return to menu button
        pygame.draw.rect(self.game_screen, 'Grey', self.return_to_menu_rect)
        self.game_screen.blit(return_to_menu_text, return_to_menu_text_rect)
        # quit button
        pygame.draw.rect(self.game_screen, 'Grey', self.pause_quit_rect)
        self.game_screen.blit(quit_menu_text, quit_menu_text_rect)
        
    def game_over_scene(self, final_score, final_time):

        pygame.display.set_caption("Game Over")

        gameover_text = self.game_font.render(
            f"GAME OVER!",
            True,
            'Black').convert_alpha()
        gameover_text_rect = gameover_text.get_rect(center=(500, 100))

        gameover_score = self.game_font.render(
            f"Final score: {final_score}, Final time: {final_time[:-4]}",
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

    def final_scene(self, final_score, final_time):

        pygame.display.set_caption("Final")
        pygame.display.update()

        congrats_text = self.game_font.render(
            f"Congratulations, you beat the game!",
            True,
            'Black').convert_alpha()
        congrats_text_rect = congrats_text.get_rect(center=(500, 100))

        continue_text = self.game_font.render(
            f"Your final score: {final_score}, Final time: {final_time[:-4]}",
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
