import os
from dotenv import load_dotenv
import logging
import pygame
from UI.scenes import GameScenes
from utils.utils import time_str_to_seconds, centiseconds_to_time
from backend.server.requests import RequestHandler
import json
from config.config import DREAMLO_API_URL

load_dotenv(os.path.join(os.path.dirname(__file__), "..", "..", ".venv", ".env"))
DREAMLO_PUBLIC_KEY = os.getenv("DREAMLO_PUBLIC_KEY")

class GameLeaderboard(GameScenes):
    def __init__(self):
        super().__init__()
        self.leaderboard_data_fetched = False  # Flag to track if data has been fetched
        self.leaderboard_data = []  # Store fetched leaderboard data
        self.running = False

    async def fetch_leaderboard_data(self):
        """
        Fetch leaderboard data from Dreamlo and store it for display.
        """
        if not all([DREAMLO_PUBLIC_KEY]):
            logging.error("Dreamlo public key is missing.")
            return

        url = f"{DREAMLO_API_URL}/{DREAMLO_PUBLIC_KEY}/json"
        data = RequestHandler()

        scores = await data.get(url)
        scores_list = json.loads(scores)

        leaderboard_data = (
            scores_list.get("dreamlo", {}).get("leaderboard", {}).get("entry", [])
        )

        if not isinstance(leaderboard_data, list):
            leaderboard_data = [leaderboard_data]  # Handle single entry case

        self.leaderboard_data = sorted(
            leaderboard_data,
            key=lambda x: time_str_to_seconds(x.get("seconds", "99:99:99.99")),
        )[:3]

        self.leaderboard_data_fetched = True  # Mark data as fetched

    async def display_leaderboard(self):
        pygame.display.set_caption("Leaderboard")

        leaderboard_screen_text = self.game_font.render(
            "RavensKiller Leaderboard:", True, "Black"
        ).convert_alpha()
        leaderboard_screen_text_rect = leaderboard_screen_text.get_rect(
            center=(500, 50)
        )

        refresh_data_text = self.game_font.render(
            "Refresh Data", True, "Black"
        ).convert_alpha()
        refresh_data_text_rect = refresh_data_text.get_rect(
            center=self.refresh_leaderboard_rect.center
        )

        back_leaderboard_text = self.game_font.render(
            "Back", True, "Black"
        ).convert_alpha()
        back_leaderboard_text_rect = back_leaderboard_text.get_rect(
            center=self.back_leaderboard_rect.center
        )

        # Fetch leaderboard data only if it hasn't been fetched yet
        if not self.leaderboard_data_fetched:
            await self.fetch_leaderboard_data()  # Properly await the coroutine

        if self.running:
            self.game_screen.blit(self.image, (0, 0))
            self.game_screen.blit(leaderboard_screen_text, leaderboard_screen_text_rect)

            # Refresh button
            pygame.draw.rect(self.game_screen, "Grey", self.refresh_leaderboard_rect)
            self.game_screen.blit(refresh_data_text, refresh_data_text_rect)

            # Back button
            pygame.draw.rect(self.game_screen, "Grey", self.back_leaderboard_rect)
            self.game_screen.blit(back_leaderboard_text, back_leaderboard_text_rect)

            # Display leaderboard data
            y_offset = 125
            for rank, player in enumerate(self.leaderboard_data, start=1):
                username = player.get("name", "Unknown")
                highest_score = player.get("score", "0")
                best_time_seconds = player.get("seconds", "N/A")
                best_time_formatted = centiseconds_to_time(int(best_time_seconds))

                player_text = self.game_font.render(
                    f"{rank}. {username} - Score: {highest_score}, Best Time: {best_time_formatted}",
                    True,
                    "Black",
                ).convert_alpha()

                player_divider = self.game_font.render(
                    f"{'-' * round(player_text.get_width() / self.game_font.size('-')[0])}",
                    True,
                    "Black",
                )

                player_text_rect = player_text.get_rect(center=(500, y_offset))
                player_divider_rect = player_text.get_rect(center=(500, y_offset + 30))
                self.game_screen.blit(player_text, player_text_rect)
                self.game_screen.blit(player_divider, player_divider_rect)
                y_offset += 60

            pygame.display.update()
