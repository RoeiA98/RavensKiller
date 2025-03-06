import pygame
from UI.scenes import GameScenes
from backend.database.db_handler import create_connection

class GameLeaderboard(GameScenes):
    def __init__(self):
        super().__init__()
        
    def fetch_leaderboard_data(self):
        # Fetch leaderboard data from the database
        db = create_connection()
        if db is not None:
            collection = db['game_scores']
            leaderboard_data = collection.find().sort("highest_score", -1).limit(10)  # Get top 10 scores

            y_offset = 150
            for rank, player in enumerate(leaderboard_data, start=1):
                player_text = self.game_font.render(
                    f"{rank}. {player['username']} - Score: {player['highest_score']}, Level: {player['highest_level']}, Best Time: {player.get('best_time', {player['best_time']})}",
                    True,
                    'Black'
                ).convert_alpha()
                player_text_rect = player_text.get_rect(center=(500, y_offset))
                self.game_screen.blit(player_text, player_text_rect)
                y_offset += 40
    
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

