import pygame

from GameOrigin.Modes import GameModes
from GameOrigin.Spawns import set_spawn_rate
import asyncio
from Sprites.Player import Player
from UI.FPS import FPS
from UI.Levels import *


class GameLevels(GameModes):

    def __init__(self):
        super().__init__()

        self.keys = pygame.key.get_pressed()
        self.game_font = pygame.font.Font('Fonts/Amatic-Bold.ttf', 40)
        self.level_text = None
        self.objective_text = None
        self.objective_text_rect = None
        self.progress_text = None
        self.progress_text_rect = None
        self.level_text_rect = None
        self.objective2_text = None
        self.objective2_text_rect = None
        self.fps = FPS()

    async def run_game(self):

        while not self.game_running:
            self.game_scenes.game_intro()
            self.game_running = self.game_start()
            pygame.display.update()
            await asyncio.sleep(0)

        self.game_active_status = True
        self.player.add(Player())  # player draw

        while self.game_running:
            if self.game_active_status:
                self.levels_handler()
            elif self.continue_screen:
                self.load_next_level()
            else:
                # End game and reset levels
                self.game_over()
                self.game_restart()

            if not self.game_pause:
                self.fps.render(self.game_screen)
            pygame.display.update()
            self.fps.clock.tick(self.MAX_FPS)
            await asyncio.sleep(0)

    def stop_level(self):
        self.continue_screen = True
        self.game_active_status = False
        self.current_level += 1

    def load_next_level(self):

        if self.current_level >= len(self.game_level_scenes):
            self.game_scenes.final_scene(self.display_player_score.current_score)
        else:
            self.game_scenes.next_level()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:

                if self.current_level >= len(self.game_level_scenes):
                    self.display_player_score.current_score = 0
                    self.current_level = 1

                self.continue_screen = False
                self.game_current_level_scene = self.game_level_scenes[self.current_level]
                self.game_reset()

    def levels_handler(self):
        if self.current_level == 1:
            self.level_one()
        elif self.current_level == 2:
            self.level_two()
        elif self.current_level == 3:
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
            self.stop_level()

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
            self.stop_level()

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
            self.stop_level()

    def level_four(self):
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
            self.stop_level()