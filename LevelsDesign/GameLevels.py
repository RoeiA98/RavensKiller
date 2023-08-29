import pygame

from GameOrigin.Modes import GameModes
from GameOrigin.Spawns import set_spawn_rate
from Sprites.Player import Player
from UI.Levels import *


class GameLevels(GameModes):

    def __init__(self):
        super().__init__()

        self.game_active_status = self.game_scenes.game_intro()
        self.player.add(Player())  # player draw

    def next_level(self):

        self.game_reset()
        self.current_level += 1

        if self.current_level >= len(self.game_level_scenes):
            self.game_active_status = self.game_scenes.final_scene(self.display_player_score.current_score)
            self.display_player_score.current_score = 0
            self.current_level = 1
        else:
            self.game_active_status = self.game_scenes.next_level()

        self.game_current_level_scene = self.game_level_scenes[self.current_level]

    def levels_handler(self):
        if self.current_level == 1:
            print(f"global var: {self.ground_ravens_kills}")
            print(f"local var: {self.game_current_level_scene.gr_kills}")
            self.level_one()
        elif self.current_level == 2:
            print(f"global var: {self.ground_ravens_kills}")
            print(f"local var: {self.game_current_level_scene.gr_kills}")
            self.level_two()
        elif self.current_level == 3:
            print(f"global var: {self.ground_ravens_kills}")
            print(f"local var: {self.game_current_level_scene.gr_kills}")
            self.level_three()
        elif self.current_level == 4:
            self.level_four()

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
                    self.game_current_level_scene.gr_kills += 1

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1

        if self.game_current_level_scene.gr_kills == 5:
            self.next_level()

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
                    self.game_current_level_scene.gr_kills += 1

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1

        if self.game_current_level_scene.gr_kills == 15:
            self.next_level()

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
            self.next_level()

    def level_four(self):
        """
        Level logic:
            Objective:  - Kill 5 fly ravens without taking damage

        """

        """Level settings:"""
        self.collisions.fly_raven_damage = 100

        self.spawns.fly_raven_spawn = set_spawn_rate(1000, 2000)
        self.spawns.deadly_raven_spawn = set_spawn_rate(10000, 15000)

        self.events_handler()

        """Level display:"""
        self.game_active()

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1
            self.game_current_level_scene.fl_kills += 1

        if self.game_current_level_scene.fl_kills == 5:
            self.next_level()

    def level_five(self):
        """
        Level logic:
            Objective:  - Kill 10 Ground Ravens

        """

        """Level settings:"""
        self.ground_raven_hp = 200
        self.collisions.fly_raven_damage = 35
        self.collisions.ground_raven_damage = 30

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

                    if self.game_current_level_scene.gr_kills < 10:
                        self.game_current_level_scene.gr_kills += 1

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1
            if self.game_current_level_scene.fl_kills < 3:
                self.game_current_level_scene.fl_kills += 1

        if self.game_current_level_scene.gr_kills == 10 \
                and self.game_current_level_scene.fl_kills == 3:
            self.next_level()
