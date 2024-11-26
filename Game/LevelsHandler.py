import pygame # type: ignore
import asyncio
import importlib
import os
from SpritesLogic.player import Player
from Game.setup import *
from UI.GameScenes import *
from SpritesLogic.player import *
from Game.spawns import *
from sys import exit
from UI.score import *

class LevelsHandler(Game):

    def __init__(self):
        super().__init__()
        
        # Dynamically import all modules in the Levels folder
        levels_path = os.path.join(os.path.dirname(__file__), '..', 'Levels')
        excluded_files = {"__init__.py"}

        modules = {
            f.split(".")[0]: importlib.import_module(f"Levels.{f[:-3]}")
            for f in os.listdir(levels_path)
            if f.endswith(".py") and f not in excluded_files
        }

        # Sort and populate levels and scenes
        self.levels = [None] + [getattr(module, name) for name, module in sorted(modules.items())]
        self.game_level_scenes = self.levels[0:]
        # Setting current level
        self.game_current_level_scene = self.game_level_scenes[self.current_level]

    def handler(self):
        self.levels[self.current_level].play(self)
        
    def events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.game_active_status:
                # bullets shoot
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not self.game_pause:
                    self.bullet.add(shoot_bullet(self.player.sprite.rect.x,
                                                 self.player.sprite.rect.y,
                                                 self.player.sprite.player_current_direction))

                # Pause logic
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if self.game_pause:
                        self.game_pause = False
                    else:
                        self.game_pause = True
                        self.game_scenes.pause_screen()

    def game_start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                pygame.time.delay(100)
                return True

    def game_reset(self):
        # Deleting enemies
        self.fly_raven_group.empty()
        self.ground_raven_group.empty()
        self.deadly_raven_group.empty()
        self.all_enemies.empty()
        # Resetting player
        self.player.sprite.player_reset_pos()
        self.player_health.hp = 100
        self.bullet.empty()
        # Resetting score
        self.ground_ravens_kills = 0
        self.fly_ravens_kills = 0
        
        self.game_active_status = True

    def game_restart(self):
        for intro_event in pygame.event.get():
            if intro_event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if intro_event.type == pygame.KEYDOWN and intro_event.key == pygame.K_RETURN:
                self.game_reset()
                self.display_player_score.current_score = 0

    def game_over(self):
        # Reset score
        self.ground_ravens_kills = 0
        self.fly_ravens_kills = 0
        # Deleting enemies
        self.fly_raven_group.empty()
        self.ground_raven_group.empty()
        self.deadly_raven_group.empty()
        self.all_enemies.empty()
        self.bullet.empty()
        # Resetting player position
        self.player.sprite.rect = self.player.sprite.image.get_rect(midbottom=(500, 450))
        # Game over scene
        self.game_scenes.game_over_scene(self.display_player_score.current_score)
        self.current_level = 1
        self.game_current_level_scene = self.game_level_scenes[self.current_level]
        self.game_active_status = False

    def game_active(self):
        if not self.game_pause:
            # Display game
            self.game_scenes.game_active()
            self.levels[self.current_level].display_level(self, self.game_screen)
            self.game_current_level_scene.update(self, self.game_screen)
            self.fps.render(self.game_screen)
        
            # Score
            self.display_player_score.update(self.game_screen)

            # Player
            self.player.draw(self.game_screen)
            self.player.update()
            self.player_health.draw(self.game_screen)
            self.player_health.draw_hp_text(self.game_screen)

            # Enemy
            self.all_enemies.update()
            self.all_enemies.draw(self.game_screen)

            self.spawns.spawn_fly_raven()
            self.spawns.spawn_deadly_raven()
            self.spawns.spawn_ground_raven(self.ground_raven_hp)

            # Bullet
            self.bullet.draw(self.game_screen)
            self.bullet.update()

            # Collision
            self.game_active_status = self.collisions.detect_collision()
            # self.game_active_status = True  # for testings without collision
            
    def stop_level(self):
        self.continue_screen = True
        self.game_active_status = False
        self.current_level += 1

    def load_next_level(self):
        if self.current_level >= len(self.game_level_scenes):
            self.final_level = True
            self.game_scenes.final_scene(self.display_player_score.current_score)
        else:
            self.game_scenes.next_level(self.current_level, len(self.game_level_scenes))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                
                # restarting to level 1
                if self.current_level >= len(self.game_level_scenes):
                    self.display_player_score.current_score = 0
                    self.current_level = 1
                    self.final_level = False

                self.continue_screen = False
                self.game_current_level_scene = self.game_level_scenes[self.current_level]
                self.game_reset()
    
    def display_level(self, screen):
        pass
            
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
                self.handler()
            elif self.continue_screen:
                self.load_next_level()
            else:
                self.game_over()
                self.game_restart()

            pygame.display.update()
            self.fps.clock.tick(self.MAX_FPS)
            await asyncio.sleep(0)