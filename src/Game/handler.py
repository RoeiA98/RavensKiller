from datetime import timedelta
import pygame  # type: ignore
import asyncio
from src.SpritesLogic.player import Player
from src.Game.setup import *
from UI.scenes import *
from UI.intro import *
from src.SpritesLogic.player import *
from src.Game.spawns import *
from sys import exit
from UI.score import *
from utils.utils import import_levels
from database.dbhandler import app, save_score

class Handler(Game):

    def __init__(self):
        super().__init__()
        
        # import and sort levels
        self.levels = [None] + [getattr(module, name) for name, module in sorted(import_levels("Levels").items())]
        self.game_level_scenes = self.levels[0:]
        # set current level
        self.game_current_level_scene = self.game_level_scenes[self.current_level]
        
        self.start_time = 0
        self.paused_time = 0
        self.elapsed_time = 0
        self.last_pause_time = 0
        self.elapsed_time_ms = 0

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
                    self.bullet.add(Player.player_shoot_bullet(self, self.player.sprite.rect.x,
                                                 self.player.sprite.rect.y,
                                                 self.player.sprite.player_current_direction))

                # pause logic
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if self.game_pause:
                        self.game_pause = False
                        self.paused_time += pygame.time.get_ticks() - self.last_pause_time
                    else:
                        self.game_pause = True
                        self.last_pause_time = pygame.time.get_ticks()
                        self.game_scenes.pause_screen()
        
    def reset_timer(self):
        self.elapsed_time = 0
        self.paused_time = 0
        self.last_pause_time = 0
        self.elapsed_time_ms = 0
        self.start_time = pygame.time.get_ticks()

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

    def game_restart(self):
        for intro_event in pygame.event.get():
            if intro_event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if intro_event.type == pygame.KEYDOWN and intro_event.key == pygame.K_RETURN:
                self.save_to_db()
                self.game_reset()
                self.current_level = 1
                self.display_player_score.current_score = 0
                self.game_active_status = True
                self.reset_timer()

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
        self.game_scenes.game_over_scene(self.display_player_score.current_score, str(self.elapsed_time))
        self.game_current_level_scene = self.game_level_scenes[self.current_level]
        self.game_active_status = False
    
    def save_to_db(self):
        # saving to database
        with app.app_context():
            save_score(self.game_intro.name_input, 
                        self.display_player_score.current_score, 
                        str(self.elapsed_time)[:-4], 
                        self.current_level - 1 if self.current_level >= len(self.game_level_scenes) else self.current_level
            )

    def game_active(self):
        if not self.game_pause:
            # Display game
            self.game_scenes.game_active()
            self.levels[self.current_level].display_level(self, self.game_screen)
            self.game_current_level_scene.update(self, self.game_screen)
            self.fps.render(self.game_screen)
            self.game_intro.display_user_name()
            
            # Timer
            self.elapsed_time_ms = pygame.time.get_ticks() - self.start_time - self.paused_time
            self.elapsed_time = timedelta(milliseconds=self.elapsed_time_ms)
            self.timer.display_timer(self.game_screen, self.elapsed_time)
        
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
        self.last_pause_time = pygame.time.get_ticks()
        self.game_active_status = False
        self.current_level += 1

    def load_next_level(self):
        self.game_reset()
        if self.current_level >= len(self.game_level_scenes):
            self.final_scene = True
            self.game_scenes.final_scene(self.display_player_score.current_score, str(self.elapsed_time))
        else:
            self.game_scenes.next_level(self.current_level, len(self.game_level_scenes))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                self.save_to_db()
                # restarting to level 1 if user beat the game
                if self.current_level >= len(self.game_level_scenes):
                    self.display_player_score.current_score = 0
                    self.current_level = 1
                    self.final_scene = False
                    self.reset_timer()
                else:
                    self.paused_time += pygame.time.get_ticks() - self.last_pause_time

                self.continue_screen = False
                self.game_current_level_scene = self.game_level_scenes[self.current_level]
                self.game_active_status = True
            