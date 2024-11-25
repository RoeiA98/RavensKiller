import pygame # type: ignore
from Game.setup import *
from Game.spawns import set_spawn_rate

class Level3(Game):

    def __init__(self):
        super().__init__()

    def play(self):
        """
        Level logic:
            Objective:  - Kill 10 ground ravens --> not spawning ground ravens when goal reached
                        - Kill 3 fly ravens

        """

        """Level settings:"""
        self.ground_raven_hp = 170
        self.collisions.fly_raven_damage = 30
        self.collisions.ground_raven_damage = 25
        
        if self.ground_ravens_kills < 10:
            self.spawns.ground_raven_spawn = set_spawn_rate(1300, 2100)
        else:
            self.spawns.ground_raven_spawn = 0

        self.spawns.fly_raven_spawn = set_spawn_rate(1000, 2000)
        self.spawns.deadly_raven_spawn = set_spawn_rate(4000, 15000)

        self.events_handler()

        """Level display:"""
        self.game_active()

        self.hits = pygame.sprite.groupcollide(self.bullet, self.ground_raven_group, True, False)
        for bullet, hit_enemies in self.hits.items():
            for enemy in hit_enemies:
                enemy.health -= self.player.sprite.player_damage
                if enemy.health <= 0:
                    enemy.kill()
                    self.display_player_score.current_score += 1
                    self.active_game_score += 1
                    if self.ground_ravens_kills < 10:
                        self.ground_ravens_kills += 1

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1
            if self.fly_ravens_kills < 3:
                self.fly_ravens_kills += 1

        if self.ground_ravens_kills == 10 \
                and self.fly_ravens_kills == 3:
            self.stop_level()
            
    def display_level(self, screen):
        pygame.display.set_caption("Level 3")
        # Text
        self.level_text = self.game_font.render(
            "Level 3",
            True,
            'Black'
        ).convert_alpha()
        self.level_text_rect = self.level_text.get_rect(center=(800, 50))

        # Objectives
        self.objective_text = self.game_font.render(
            f"- Kill 10 Ground Ravens   {self.ground_ravens_kills}/10",
            True,
            'green' if self.ground_ravens_kills == 10 else 'black').convert_alpha()
        self.objective_text_rect = self.objective_text.get_rect(center=(780, 100))

        self.objective2_text = self.game_font.render(
            f"- Kill 3 Fly Ravens                 {self.fly_ravens_kills}/3",
            True,
            'green' if self.fly_ravens_kills == 3 else 'black').convert_alpha()
        self.objective2_text_rect = self.objective_text.get_rect(center=(780, 140))

        # Text BG
        bg = pygame.Surface((330, 140))  # the size of your rect
        bg.set_alpha(128)  # alpha level
        bg.fill('black')  # this fills the entire surface
        screen.blit(bg, (620, 30))  # (0,0) are the top-left coordinates

        # Draw
        screen.blit(self.level_text, self.level_text_rect)
        screen.blit(self.objective_text, self.objective_text_rect)
        screen.blit(self.objective2_text, self.objective2_text_rect)
