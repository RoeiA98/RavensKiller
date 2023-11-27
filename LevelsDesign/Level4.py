import pygame

from GameOrigin.Spawns import set_spawn_rate
from GameOrigin.GameLevels import GameLevels


class LevelFour(GameLevels):

    def __init__(self):
        super().__init__()

    def play(self):

        """
        Level logic:
            Objective:  - Kill 5 fly ravens without taking damage

        """

        """Level settings:"""
        self.collisions.fly_raven_damage = 100

        self.spawns.deadly_raven_spawn = 0
        self.spawns.ground_raven_spawn = 0
        self.spawns.fly_raven_spawn = set_spawn_rate(1000, 2000)

        self.events_handler()

        """Level display:"""
        self.game_active()

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1
            self.game_current_level_scene.fl_kills += 1

        if self.game_current_level_scene.fl_kills == 5:
            self.stop_level()
