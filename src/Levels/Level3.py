from src.Game.setup import *
from utils.utils import set_spawn_rate

class Level3(Game):

    def __init__(self):
        super().__init__()
        
    def load_settings(self):
        """Level settings:"""
        self.spawns.ground_raven_hp = 170
        self.collisions.fly_raven_damage = 30
        self.collisions.ground_raven_damage = 25
        
        self.spawns.deadly_raven_spawn = set_spawn_rate(4000, 15000)

    def play(self):
        """
        Level logic:
            Objective:  - Kill 10 ground ravens --> not spawning ground ravens when goal reached
                        - Kill 3 fly ravens

        """
        
        if self.game_score.ground_ravens_kills < 10:
            self.spawns.ground_raven_spawn = set_spawn_rate(1300, 2100)
        else: # removing all ground ravens when reaching level target
            self.spawns.ground_raven_spawn = 0
            for gr_raven in self.ground_raven_group:
                gr_raven.kill()

        if self.game_score.fly_ravens_kills < 3:
            self.spawns.fly_raven_spawn = set_spawn_rate(1000, 2000)
        else:
            self.spawns.fly_raven_spawn = 0
            for fl_raven in self.fly_raven_group:
                fl_raven.kill()
        
        self.active_game_events_handler()

        """Level display:"""
        self.game_active()

        self.hits = pygame.sprite.groupcollide(self.bullet, self.ground_raven_group, True, False)
        for bullet, hit_enemies in self.hits.items():
            for enemy in hit_enemies:
                enemy.health -= self.player.sprite.player_damage
                if enemy.health <= 0:
                    enemy.kill()
                    self.game_score.current_score += 1
                    if self.game_score.ground_ravens_kills < 10:
                        self.game_score.ground_ravens_kills += 1

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.game_score.current_score += 1
            if self.game_score.fly_ravens_kills < 3:
                self.game_score.fly_ravens_kills += 1

        if self.game_score.ground_ravens_kills == 10 \
                and self.game_score.fly_ravens_kills == 3:
            self.stop_level()
            
    def display_objective(self, screen):
        # Text
        level_text = self.game_font.render(
            "Level 3 Objective:",
            True,
            'Black'
        ).convert_alpha()
        level_text_rect = level_text.get_rect(center=(500, 115))

        objective_text = self.game_font.render(
            f"- Kill 10 Ground Ravens",
            True,
            'Black').convert_alpha()
        objective_text_rect = objective_text.get_rect(center=(500, 185))
        
        objective2_text = self.game_font.render(
            f"- Kill 3 Fly Ravens",
            True,
            'Black').convert_alpha()
        objective2_text_rect = objective2_text.get_rect(center=(460, 255))

        # Draw
        screen.blit(level_text, level_text_rect)
        screen.blit(objective_text, objective_text_rect)
        screen.blit(objective2_text, objective2_text_rect)
            
    def display_level(self, screen):
        pygame.display.set_caption("Level 3")
        # Text
        level_text = self.game_font.render(
            "Level 3",
            True,
            'Black'
        ).convert_alpha()
        level_text_rect = level_text.get_rect(center=(800, 50))

        # Objectives
        objective_text = self.game_font.render(
            f"- Kill 10 Ground Ravens   {self.game_score.ground_ravens_kills}/10",
            True,
            'green' if self.game_score.ground_ravens_kills == 10 else 'black').convert_alpha()
        objective_text_rect = objective_text.get_rect(center=(780, 100))

        objective2_text = self.game_font.render(
            f"- Kill 3 Fly Ravens                 {self.game_score.fly_ravens_kills}/3",
            True,
            'green' if self.game_score.fly_ravens_kills == 3 else 'black').convert_alpha()
        objective2_text_rect = objective_text.get_rect(center=(780, 140))

        # Text BG
        bg = pygame.Surface((330, 140))  # the size of your rect
        bg.set_alpha(128)  # alpha level
        bg.fill('black')  # this fills the entire surface
        screen.blit(bg, (620, 30))  # (0,0) are the top-left coordinates

        # Draw
        screen.blit(level_text, level_text_rect)
        screen.blit(objective_text, objective_text_rect)
        screen.blit(objective2_text, objective2_text_rect)
