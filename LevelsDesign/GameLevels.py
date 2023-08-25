import pygame

from Game.Modes import GameModes
from Sprites.Player import Player
from Sprites.Spawns import set_spawn_rate
from UI.Levels import *


class GameLevels(GameModes):

    def __init__(self):
        super().__init__()

    def run(self):

        self.game_active_status = self.game_scenes.game_intro()
        self.player.add(Player())  # player draw

        while self.game_running:
            if self.game_active_status:
                # level logic
                if self.levels_manager == 1:
                    self.level_one()

                if self.levels_manager == 2:
                    self.level_two()

                if self.levels_manager == 3:
                    self.level_three()
            else:
                # End game and reset levels
                self.game_over()
                self.game_restart()

            pygame.display.update()
            self.clock.tick(self.MAX_FPS)  # MAX 60 FPS

    def level_one(self):
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
            self.game_next_level()
            self.game_active_status = self.game_scenes.next_level()
            self.game_reset()
            return False

    def level_two(self):
        """
        Level logic:
            Objective: Kill 15 ground ravens

        """

        """Level settings:"""
        self.ground_raven_hp = 150
        self.collisions.fly_raven_damage = 25
        self.collisions.ground_raven_damage = 20

        self.spawns.ground_raven_spawn = set_spawn_rate(1300, 2100)
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

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1

        if self.game_current_level_scene.level_score == 15:
            self.game_next_level()
            self.game_active_status = self.game_scenes.next_level()
            self.game_reset()
            return False

    def level_three(self):
        """
        Level logic:
            Objective:  - Kill 10 ground ravens --> not spawning ground ravens when goal reached
                        - Kill 3 fly ravens

        """

        """Level settings:"""
        self.ground_raven_hp = 170
        self.collisions.fly_raven_damage = 30
        self.collisions.ground_raven_damage = 25

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
            self.game_next_level()
            self.game_active_status = self.game_scenes.next_level()
            self.game_reset()
            return False
