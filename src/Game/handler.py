# /// script
# dependencies = [
#   "pymongo"
# ]
# ///

from datetime import timedelta
from game.setup import *
from Sprites.player import *
from sys import exit
from UI.score import *
from utils.utils import import_levels
from backend.database.db_handler import save_score
import pymongo

class Handler(Game):

    def __init__(self):
        super().__init__()
        # game attributes
        self.current_level = 1
        # game flags
        self.game_active_status = False
        self.continue_screen = False
        self.game_running = False
        self.final_level = False
        self.game_pause = False
        self.display_objective = False
        # import and sort levels
        self.levels = [None] + [getattr(module, name) for name, module in sorted(import_levels("Levels").items())]
        self.game_level_scenes = self.levels[0:]
        self.levels[self.current_level].load_settings(self)
        # set current level
        self.game_current_level_scene = self.game_level_scenes[self.current_level]
        # timer
        self.start_time = 0
        self.paused_time = 0
        self.elapsed_time = 0
        self.last_pause_time = 0
        self.elapsed_time_ms = 0 

    def game_handler(self):
        self.levels[self.current_level].play(self)
        
    def active_game_events_handler(self):        
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
                    self.toggle_pause()
                
                if self.game_pause and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.game_scenes.return_to_menu_rect.collidepoint(event.pos):
                        self.game_quit_to_menu()
                    if self.game_scenes.pause_quit_rect.collidepoint(event.pos):
                        pygame.quit()
                        exit()
                
    def game_quit_to_menu(self):
        self.save_to_db()
        self.game_pause = False
        self.game_intro.name_input = "" 
        self.game_score.current_score = 0
        self.game_level_reset()
        self.game_round_reset()
        self.reset_timer()
        self.game_intro.invalid_name = False
        self.game_intro.first_level_objective_staus = False
        self.game_intro.intro_screen_status = True
        self.game_active_status = False  
        self.game_running = False
    
    def toggle_pause(self):
        if self.game_pause:
            self.game_pause = False
            self.paused_time += pygame.time.get_ticks() - self.last_pause_time
        else:
            self.game_pause = True
            self.last_pause_time = pygame.time.get_ticks()
            self.game_scenes.pause_screen()
            self.timer.display_timer(self.game_screen, self.elapsed_time, 'Gray')
        
    def reset_timer(self):
        self.elapsed_time = 0
        self.paused_time = 0
        self.last_pause_time = 0
        self.elapsed_time_ms = 0
        self.start_time = pygame.time.get_ticks()

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
        if self.continue_screen:    # * if user beat level/game
            self.load_next_level()
        else:                       # * if user lost
            if self.display_objective:
                self.game_scenes.display_level1_objective()
            else:
                self.game_scenes.game_over_scene(self.game_score.current_score, str(self.elapsed_time))
                
            for intro_event in pygame.event.get():
                if intro_event.type == pygame.KEYDOWN and intro_event.key == pygame.K_RETURN:
                    if not self.display_objective:
                        self.display_objective = True
                        self.game_over()
                    elif self.display_objective:
                        self.display_objective = False
                        self.reset_timer()
                        self.game_active_status = True
    
    def game_over(self):
        self.save_to_db()
        self.game_level_reset()
        self.game_score.current_score = 0
        self.game_current_level_scene = self.game_level_scenes[self.current_level]
        self.player.sprite.rect = self.player.sprite.image.get_rect(midbottom=(500, 450))
        self.game_round_reset()
        
    def save_to_db(self):
        # saving to database
        save_score(self.game_intro.name_input, 
                   self.game_score.current_score, 
                   str(self.elapsed_time)[:-4], 
                   self.current_level - 1 if self.current_level >= len(self.game_level_scenes) else self.current_level,
                   True if self.current_level >= len(self.game_level_scenes) else False
        )

    def game_active(self):
        if not self.game_pause and self.game_active_status:
            # Display game
            self.game_scenes.game_active()
            self.levels[self.current_level].display_level(self, self.game_screen)
            self.game_current_level_scene.update(self, self.game_screen)
            self.fps.render(self.game_screen)
            self.game_intro.display_user_name()
            
            # Timer
            self.elapsed_time_ms = pygame.time.get_ticks() - self.start_time - self.paused_time
            self.elapsed_time = timedelta(milliseconds=self.elapsed_time_ms)
            self.spawns.elapsed_time = self.elapsed_time_ms
            self.timer.display_timer(self.game_screen, self.elapsed_time, 'White')
        
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
            self.game_active_status = self.collisions.detect_collision()
            # self.game_active_status = True  # for testings without collision
        
    def stop_level(self):
        self.continue_screen = True
        self.last_pause_time = pygame.time.get_ticks()
        self.game_active_status = False
        self.current_level += 1
        if self.current_level < len(self.game_level_scenes):
            self.levels[self.current_level].load_settings(self)
        else:
            self.final_level = True

    def load_next_level(self):
        self.game_round_reset()
        if self.final_level:
            self.game_scenes.final_scene(self.game_score.current_score, str(self.elapsed_time))
        elif self.display_objective:
            self.game_scenes.display_level1_objective()
        else:
            self.game_scenes.next_level(self.current_level, len(self.game_level_scenes), self.levels)
            self.timer.display_timer(self.game_screen, self.elapsed_time, 'Gray')
        
        for event in pygame.event.get():    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if self.final_level:
                    self.final_level = False
                    self.display_objective = True
                # restarting to level 1 if user beat the game
                else:
                    if self.current_level >= len(self.game_level_scenes):
                        self.save_to_db()
                        self.game_score.current_score = 0
                        self.game_level_reset()
                        self.reset_timer()
                    else:
                        self.paused_time += pygame.time.get_ticks() - self.last_pause_time

                    self.display_objective = False
                    self.game_current_level_scene = self.game_level_scenes[self.current_level]
                    self.continue_screen = False
                    self.game_active_status = True
            if (self.final_level and event.type == pygame.MOUSEBUTTONDOWN 
                and event.button == 1 and self.game_scenes.return_to_menu_rect.collidepoint(event.pos)):
                self.game_quit_to_menu()