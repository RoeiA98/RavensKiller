import pygame  # type: ignore
from UI.scenes import GameScenes

class GameLeaderboard(GameScenes):
    def __init__(self):
        super().__init__()
    
    def display_leaderboard(self):
        pygame.display.set_caption("Leadeboard")
        pygame.display.update()
        
        leaderboard_screen_text = self.game_font.render(
            "RavensKiller Leaderboard:",
            True,
            'Black').convert_alpha()
        leaderboard_screen_text_rect = leaderboard_screen_text.get_rect(center=(500, 100))

        refresh_data_text = self.game_font.render(
            "Refresh Data",
            True,
            'Black').convert_alpha()
        refresh_data_text_rect = refresh_data_text.get_rect(center=self.refresh_leaderboard_rect.center)
        
        back_leaderboard_text = self.game_font.render(
            "Back",
            True,
            'Black').convert_alpha()
        back_leaderboard_text_rect = back_leaderboard_text.get_rect(center=self.back_leaderboard_rect.center)

        self.game_screen.blit(self.image, (0, 0))
        self.game_screen.blit(leaderboard_screen_text, leaderboard_screen_text_rect)
        # refresh button
        pygame.draw.rect(self.game_screen, 'Grey', self.refresh_leaderboard_rect)
        self.game_screen.blit(refresh_data_text, refresh_data_text_rect)
        # back button
        pygame.draw.rect(self.game_screen, 'Grey', self.back_leaderboard_rect)
        self.game_screen.blit(back_leaderboard_text, back_leaderboard_text_rect)
