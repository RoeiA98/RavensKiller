import pygame
from UI.scenes import GameScenes
from backend.database.db_handler import create_connection
from utils.utils import convert_to_timedelta

class GameLeaderboard(GameScenes):
    def __init__(self):
        super().__init__()
        
    def fetch_leaderboard_data(self):
        # Fetch leaderboard data from the database
        db = create_connection()
        if db is not None:
            collection = db['game_scores']
            # leaderboard only includes players who beat the game
            leaderboard_data = list(collection.find({"beat_game": {"$eq": True}}).sort({'best_time': 1}).limit(3))

            y_offset = 125
            for rank, player in enumerate(leaderboard_data, start=1):
                player_text = self.game_font.render(
                    f"{rank}. {player['username']} - Score: {player['highest_score']}, Best Time: {player.get('best_time', {player['best_time']})}",
                    True,
                    'Black'
                ).convert_alpha()
                player_divider = self.game_font.render(
                    f"{'-' * int((player_text.get_width() / self.game_font.size('-')[0]))}",
                    True,
                    'Black'
                )
                player_text_rect = player_text.get_rect(center=(500, y_offset))
                player_divider_rect = player_text.get_rect(center=(500, y_offset+30))
                self.game_screen.blit(player_text, player_text_rect)
                self.game_screen.blit(player_divider, player_divider_rect)
                y_offset += 60
    
    def display_leaderboard(self):
        pygame.display.set_caption("Leaderboard")
        pygame.display.update()
        
        leaderboard_screen_text = self.game_font.render(
            "RavensKiller Leaderboard:",
            True,
            'Black').convert_alpha()
        leaderboard_screen_text_rect = leaderboard_screen_text.get_rect(center=(500, 50))

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

        self.fetch_leaderboard_data()

