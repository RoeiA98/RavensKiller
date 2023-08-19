import pygame

from Game.Modes import GameModes
from Sprites.Player import Player
from Sprites.Spawns import set_spawn_rate
from UI.Levels import *


class GameLevels(GameModes):

    def game_run(self):

        self.game_active_status = self.game_scenes.game_intro()
        self.player.add(Player())  # player draw

        while self.game_running:
            if self.game_active_status:
                # level logic
                if self.levels_manager == 1:
                    self.level_one()

                if self.levels_manager == 2:
                    self.level_two()
            else:
                # End game and reset levels
                self.game_over()
                self.game_restart()

            pygame.display.update()
            self.clock.tick(self.MAX_FPS)  # MAX 60 FPS

    def level_one(self):

        """Level settings:"""
        self.ground_raven_hp = 100
        self.collisions.fly_raven_damage = 30
        self.collisions.ground_raven_damage = 25

        self.spawns.ground_raven_spawn = set_spawn_rate(1300, 2100)
        self.spawns.fly_raven_spawn = set_spawn_rate(2400, 3000)
        self.spawns.deadly_raven_spawn = set_spawn_rate(4000, 15000)

        self.events_handler()

        """Level display:"""
        self.game_active()

        """
        Level logic:
            Objective: Killing 5 ground ravens

        """
        self.hits = pygame.sprite.groupcollide(self.bullet, self.ground_raven_group, True, False)
        for bullet, hit_enemies in self.hits.items():
            for enemy in hit_enemies:
                enemy.health -= self.player.sprite.player_damage
                if enemy.health <= 0:
                    enemy.kill()
                    self.display_player_score.current_score += 1
                    self.game_current_level.level_score += 1
                    if self.game_current_level.level_score == 5:
                        self.game_next_level()
                        self.game_active_status = self.game_scenes.next_level()
                        self.game_reset()
                        return False

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1

    def level_two(self):

        """Level settings:"""
        self.ground_raven_hp = 150
        self.collisions.fly_raven_damage = 30
        self.collisions.ground_raven_damage = 25

        self.spawns.ground_raven_spawn = set_spawn_rate(1300, 2100)
        self.spawns.fly_raven_spawn = set_spawn_rate(1000, 2000)
        self.spawns.deadly_raven_spawn = set_spawn_rate(4000, 15000)
        self.events_handler()

        """Level display:"""
        self.game_active()

        """
        Level logic:
            Objective: Killing 15 ground ravens

        """
        self.hits = pygame.sprite.groupcollide(self.bullet, self.ground_raven_group, True, False)
        for bullet, hit_enemies in self.hits.items():
            for enemy in hit_enemies:
                enemy.health -= self.player.sprite.player_damage
                if enemy.health <= 0:
                    enemy.kill()
                    self.display_player_score.current_score += 1
                    self.game_current_level.level_score += 1
                    if self.game_current_level.level_score == 15:
                        self.game_next_level()
                        self.game_active_status = self.game_scenes.next_level()
                        self.game_reset()
                        return False

        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1
