import pygame

from GameOrigin.Spawns import set_spawn_rate
from GameOrigin.GameLevels import GameLevels


class LevelThree(GameLevels):

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

        # not spawning ground ravens when goal reached
        if self.game_current_level_scene.gr_kills < 10:
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
                    self.game_current_level_scene.level_score += 1

                    if self.game_current_level_scene.gr_kills < 10:
                        self.game_current_level_scene.gr_kills += 1

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1
            if self.game_current_level_scene.fl_kills < 3:
                self.game_current_level_scene.fl_kills += 1

        if self.game_current_level_scene.gr_kills == 10 \
                and self.game_current_level_scene.fl_kills == 3:
            self.stop_level()
