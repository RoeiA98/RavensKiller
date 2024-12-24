import pygame # type: ignore
from utils.utils import set_spawn_rate
from src.Game.setup import *

class Level1(Game):

    def __init__(self):
        super().__init__()
        
    def load_settings(self):
        """Level settings:"""
        self.spawns.ground_raven_hp = 100
        self.collisions.fly_raven_damage = 20
        self.collisions.ground_raven_damage = 15
        self.spawns.ground_raven_spawn = set_spawn_rate(1300, 2100)
        self.spawns.fly_raven_spawn = set_spawn_rate(2400, 3000)
        self.spawns.deadly_raven_spawn = set_spawn_rate(4000, 15000)
        
    def play(self):
        """
        Level logic:
            Objective: Kill 5 ground ravens

        """
        self.active_game_events_handler()

        """Level display:"""
        self.game_active()

        self.hits = pygame.sprite.groupcollide(
            self.bullet, self.ground_raven_group, True, False
        )
        for bullet, hit_enemies in self.hits.items():
            for enemy in hit_enemies:
                enemy.health -= self.player.sprite.player_damage
                if enemy.health <= 0:
                    enemy.kill()
                    self.game_score.current_score += 1
                    self.game_score.ground_ravens_kills += 1

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.game_score.current_score += 1

        if self.game_score.ground_ravens_kills == 5:
            self.stop_level()
            
    def display_objective(self, screen):
        # Text
        level_text = self.game_font.render(
            "Level 1 Objective:",
            True,
            'Black'
        ).convert_alpha()
        level_text_rect = level_text.get_rect(center=(500, 115))

        objective_text = self.game_font.render(
            f"- Kill 5 Ground Ravens",
            True,
            'Black').convert_alpha()
        objective_text_rect = objective_text.get_rect(center=(500, 185))

        # Draw
        screen.blit(level_text, level_text_rect)
        screen.blit(objective_text, objective_text_rect)
            
    def display_level(self, screen):
        pygame.display.set_caption("Level 1")
        # Text
        level_text = self.game_font.render(
            "Level 1",
            True,
            'Black'
        ).convert_alpha()
        level_text_rect = level_text.get_rect(center=(800, 50))

        objective_text = self.game_font.render(
            f"- Kill 5 Ground Ravens",
            True,
            'Black').convert_alpha()
        objective_text_rect = objective_text.get_rect(center=(780, 100))

        progress_text = self.game_font.render(
            f"Ground Ravens Killed: {self.game_score.ground_ravens_kills}",
            True,
            'Black').convert_alpha()
        progress_text_rect = progress_text.get_rect(center=(800, 150))

        # Text BG
        bg = pygame.Surface((300, 100))  # the size of your rect
        bg.set_alpha(128)  # alpha level
        bg.fill('black')  # this fills the entire surface
        screen.blit(bg, (650, 30))  # coordinates

        # Draw
        screen.blit(level_text, level_text_rect)
        screen.blit(objective_text, objective_text_rect)
        screen.blit(progress_text, progress_text_rect)