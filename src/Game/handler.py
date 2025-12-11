import pygame
from src.Sprites.player import Player
from src.Game.game import *
from UI.scenes import *
from UI.intro import *
from src.Sprites.player import *
from sys import exit
from UI.score import *
from utils.Utils import import_levels
from backend.database.db_handler import save_score
import asyncio
from src.Game.game_state import GameStateManager, GameState
from src.Game.timer import GameTimer


class Handler(Game):

    def __init__(self):
        super().__init__()
        # game state manager
        self.state_manager = GameStateManager()
        # game attributes
        self.current_level = 1
        # game flags
        self.final_level = False
        # import and sort levels
        self.levels = [None] + [getattr(module, name) for name, module in sorted(import_levels("Levels").items())]
        self.game_level_scenes = self.levels[0:]
        self.levels[self.current_level].load_settings(self)
        # set current level
        self.game_current_level_scene = self.game_level_scenes[self.current_level]
        # timer
        self.game_timer = GameTimer()
        

    def game_handler(self):
        self.levels[self.current_level].play(self)

    def active_game_events_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.state_manager.is_state(GameState.PLAYING):
                # bullets shoot
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
                    self.bullet.add(
                        Player.player_shoot_bullet(self, self.player.sprite.rect.x, self.player.sprite.rect.y, self.player.sprite.player_current_direction))
                # pause logic
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.toggle_pause()

            if (self.state_manager.is_state(GameState.PAUSED) and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                if self.game_scenes.return_to_menu_rect.collidepoint(event.pos):
                    self.game_quit_to_menu()
                if self.game_scenes.pause_quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()

    def game_quit_to_menu(self):
        self.save_to_db_sync()
        self.state_manager.change_state(GameState.INTRO)
        self.game_intro.name_input = ""
        self.game_score.current_score = 0
        self.game_level_reset()
        self.game_round_reset()
        self.reset_timer()
        self.game_intro.invalid_name = False
        self.game_intro.first_level_objective_staus = False
        self.game_intro.intro_screen_status = True

    def toggle_pause(self):
        if self.state_manager.is_state(GameState.PAUSED):
            self.state_manager.change_state(GameState.PLAYING)
            self.game_timer.resume()
        else:
            self.state_manager.change_state(GameState.PAUSED)
            self.game_timer.pause()

    def handle_pause_state(self):
        """Handle pause state rendering and events"""
        self.game_scenes.pause_screen()
        self.timer.display_timer(self.game_screen, self.game_timer.get_elapsed_time(), "Gray")
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.toggle_pause()
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.game_scenes.return_to_menu_rect.collidepoint(event.pos):
                    self.game_quit_to_menu()
                if self.game_scenes.pause_quit_rect.collidepoint(event.pos):
                    pygame.quit()
                    exit()

    def reset_timer(self):
        self.game_timer.reset()
        self.game_timer.start()

    def game_round_reset(self):
        # Deleting enemies and resetting their spawns
        self.fly_raven_group.empty()
        self.ground_raven_group.empty()
        self.deadly_raven_group.empty()
        self.all_enemies.empty()
        self.spawns.reset_all_last_spawns()
        # Resetting player
        self.player.sprite.player_reset_pos()
        self.player_health.hp = 100
        self.bullet.empty()
        # Resetting score
        self.game_score.ground_ravens_kills = 0
        self.game_score.fly_ravens_kills = 0

    def game_level_reset(self):
        self.current_level = 1
        self.levels[self.current_level].load_settings(self)

    def game_stop(self):
        if self.state_manager.is_state(GameState.NEXT_LEVEL):  # * if user beat level/game
            self.load_next_level()
        else:  # * if user lost
            if self.state_manager.is_state(GameState.DISPLAY_OBJECTIVE):
                self.game_scenes.display_level1_objective()
            else:
                self.game_timer.pause()
                self.game_scenes.game_over_scene(self.game_score.current_score, str(self.game_timer.get_elapsed_time()))

            for intro_event in pygame.event.get():
                if (intro_event.type == pygame.KEYDOWN and intro_event.key == pygame.K_RETURN):
                    if not self.state_manager.is_state(GameState.DISPLAY_OBJECTIVE):
                        self.state_manager.change_state(GameState.DISPLAY_OBJECTIVE)
                        self.game_over()
                    elif self.state_manager.is_state(GameState.DISPLAY_OBJECTIVE):
                        self.state_manager.change_state(GameState.PLAYING)
                        self.reset_timer()

    def game_over(self):
        self.save_to_db_sync()
        self.game_level_reset()
        self.game_score.current_score = 0
        self.game_current_level_scene = self.game_level_scenes[self.current_level]
        self.player.sprite.rect = self.player.sprite.image.get_rect(midbottom=(500, 450))
        self.game_round_reset()

    def save_to_db_sync(self):
        elapsed_time_str = str(self.game_timer.get_elapsed_time())[:-4]
        print(f"elapsed_time before SENDING!!: {elapsed_time_str}")
        asyncio.create_task(
            save_score(
                self.game_intro.name_input,
                self.game_score.current_score,
                elapsed_time_str,
                (self.current_level - 1 if self.current_level >= len(self.game_level_scenes) else self.current_level),
                True if self.current_level >= len(self.game_level_scenes) else False,
            )
        )

    def game_active(self):
        if self.state_manager.is_state(GameState.PLAYING):
            # Display game
            self.game_scenes.game_active()
            self.levels[self.current_level].display_level(self, self.game_screen)
            self.game_current_level_scene.update(self, self.game_screen)
            self.fps.render(self.game_screen)
            self.game_intro.display_user_name()
            # Timer
            elapsed_time_ms = self.game_timer.get_elapsed_time_ms()
            elapsed_time = self.game_timer.get_elapsed_time()
            self.spawns.elapsed_time = elapsed_time_ms
            self.timer.display_timer(self.game_screen, elapsed_time, "White")
            # Score
            self.game_score.update(self.game_screen)
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
            self.spawns.spawn_ground_raven()
            # Bullet
            self.bullet.draw(self.game_screen)
            self.bullet.update()
            # Collision
            collision_result = self.collisions.detect_collision()
            if not collision_result:
                self.state_manager.change_state(GameState.GAME_OVER)
            # self.state_manager.change_state(GameState.PLAYING)  # for testings without collision

    def stop_level(self):
        self.state_manager.change_state(GameState.NEXT_LEVEL)
        self.game_timer.pause()
        self.current_level += 1
        if self.current_level < len(self.game_level_scenes):
            self.levels[self.current_level].load_settings(self)
        else:
            self.final_level = True

    def load_next_level(self):
        self.game_round_reset()
        if self.final_level:
            self.game_scenes.final_scene(self.game_score.current_score, str(self.game_timer.get_elapsed_time()))
        else:
            self.game_scenes.next_level(self.current_level, len(self.game_level_scenes), self.levels)
            self.timer.display_timer(self.game_screen, self.game_timer.get_elapsed_time(), "Gray")

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if self.final_level:
                    # User completed the final level - show objective screen before restarting
                    self.final_level = False
                    self.save_to_db_sync()
                    self.game_score.current_score = 0
                    self.game_level_reset()
                    self.reset_timer()
                    self.state_manager.change_state(GameState.DISPLAY_OBJECTIVE)
                    self.game_current_level_scene = self.game_level_scenes[self.current_level]
                else:
                    # Normal level progression
                    self.game_timer.resume()
                    self.state_manager.change_state(GameState.PLAYING)
                    self.game_current_level_scene = self.game_level_scenes[self.current_level]
                    
            if (self.final_level and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and self.game_scenes.return_to_menu_rect.collidepoint(event.pos)):
                self.game_quit_to_menu()