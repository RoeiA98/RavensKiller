import pygame

from GameOrigin.Spawns import set_spawn_rate
from LevelsDesign.GameLevels import GameLevels


class LevelOne(GameLevels):
    def __init__(self):
        super().__init__()
        """
        Level logic:
            Objective: Kill 5 ground ravens

        """

        """Level settings:"""
        self.ground_raven_hp = 100
        self.collisions.fly_raven_damage = 20
        self.collisions.ground_raven_damage = 15

        self.spawns.ground_raven_spawn = set_spawn_rate(1300, 2100)
        self.spawns.fly_raven_spawn = set_spawn_rate(2400, 3000)
        self.spawns.deadly_raven_spawn = set_spawn_rate(4000, 15000)

        self.events_handler()

        """Level display:"""
        self.game_active()

    def play(self):
        self.hits = pygame.sprite.groupcollide(self.bullet, self.ground_raven_group, True, False)
        for bullet, hit_enemies in self.hits.items():
            for enemy in hit_enemies:
                enemy.health -= self.player.sprite.player_damage
                if enemy.health <= 0:
                    enemy.kill()
                    self.display_player_score.current_score += 1
                    self.game_current_level_scene.level_score += 1

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1

        if self.game_current_level_scene.level_score == 5:
            self.next_level()
            self.game_active_status = self.game_scenes.next_level()
