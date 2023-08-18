import pygame
from UI import Levels
from Sprites.Scenes import *
from Sprites.Enemies import *
from Sprites.Player import *
from Sprites.Collision import *
from sys import exit
from UI.Score import *


class Game:
    def __init__(self):

        """" General Attributes """
        self.MAX_FPS = 60
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1000, 550
        self.game_screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_active_status = False
        self.game_intro_status = True
        self.game_running = True

        """" ------------------------------------------------- """

        """ Game Attributes """
        self.active_game_score = 0
        self.display_player_score = Score(self.active_game_score)

        """" ------------------------------------------------- """

        """ Enemy Attributes """
        self.hits = None
        self.all_enemies = pygame.sprite.Group()
        self.fly_raven_group = pygame.sprite.Group()
        self.ground_raven_group = pygame.sprite.Group()
        self.deadly_raven_group = pygame.sprite.Group()
        self.ground_raven_hp = 0
        self.fly_raven_spawn = 0
        self.ground_raven_spawn = 0
        self.deadly_raven_spawn = 0
        self.last_ground_raven_spawn_time = 0
        self.last_fly_raven_spawn_time = 0
        self.last_deadly_raven_spawn_time = 0

        """" ------------------------------------------------- """

        """ Scenes Attributes """
        self.levels_manager = 1
        self.game_scenes = GameScenes()
        self.game_levels = [  # level correlates with index
            None,
            Levels.LevelOne(self.active_game_score),
            Levels.LevelTwo(self.active_game_score)
        ]
        self.game_current_level = self.game_levels[self.levels_manager]

        """" ------------------------------------------------- """

        """ Player Attributes """
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.player_health = PlayerHealth(100, 100)
        self.bullet = pygame.sprite.Group()

        """" ------------------------------------------------- """

        self.collisions = CollisionsHandler(self.player,
                                            self.player_health,
                                            self.fly_raven_group,
                                            self.ground_raven_group,
                                            self.deadly_raven_group,
                                            self.all_enemies)

    def events_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.game_active_status:
                # bullets shoot
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bullet.add(Player().shoot_bullet(self.player.sprite.rect.x,
                                                          self.player.sprite.rect.y,
                                                          self.player.sprite.player_current_direction))

    def game_run(self):

        self.game_active_status = self.game_scenes.game_intro()

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

    def game_reset(self):
        # Deleting enemies
        self.fly_raven_group.empty()
        self.ground_raven_group.empty()
        self.deadly_raven_group.empty()
        self.all_enemies.empty()
        # Resetting player
        self.player.sprite.rect = self.player.sprite.image.get_rect(midbottom=(500, 450))
        self.player_health.hp = 100
        # Resetting score
        self.game_current_level.level_score = 0

        self.game_active_status = True

    def game_restart(self):
        for intro_event in pygame.event.get():
            if intro_event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if intro_event.type == pygame.KEYDOWN and intro_event.key == pygame.K_SPACE:
                self.game_reset()

    def game_next_level(self):
        self.levels_manager += 1
        self.game_current_level = self.game_levels[self.levels_manager]

    def game_over(self):
        # Deleting enemies
        self.fly_raven_group.empty()
        self.ground_raven_group.empty()
        self.deadly_raven_group.empty()
        self.all_enemies.empty()
        # Resetting player position
        self.player.sprite.rect = self.player.sprite.image.get_rect(midbottom=(500, 450))
        # Game over scene
        self.display_player_score.current_score = 0
        self.game_scenes.game_over(self.game_current_level.level_score)
        self.levels_manager = 1
        self.game_current_level = self.game_levels[self.levels_manager]
        self.game_active_status = False

    def game_active(self):
        # Display game
        self.game_scenes.game_active()
        self.game_current_level.update(self.game_screen)

        # Score
        self.display_player_score.update(self.game_screen)

        # Player
        self.player.draw(self.game_screen)
        self.player.update()

        # Player health
        self.player_health.draw(self.game_screen)
        self.player_health.draw_hp_text(self.game_screen)

        # Enemy
        self.all_enemies.update()
        self.all_enemies.draw(self.game_screen)
        self.spawn_fly_raven()
        self.spawn_ground_raven()
        self.spawn_deadly_raven()

        # Bullet
        self.bullet.draw(self.game_screen)
        self.bullet.update()

        # Collision
        self.game_active_status = self.collisions.detect_collision()
        # self.game_active_status = True  # for testings without collision

    def spawn_fly_raven(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_fly_raven_spawn_time > self.fly_raven_spawn:
            self.last_fly_raven_spawn_time = current_time
            new_fly_raven = FlyRaven()
            self.fly_raven_group.add(new_fly_raven)
            self.all_enemies.add(new_fly_raven)

    def spawn_ground_raven(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_ground_raven_spawn_time > self.ground_raven_spawn:
            self.last_ground_raven_spawn_time = current_time
            new_ground_raven = GroundRaven(self.ground_raven_hp, self.game_screen)
            self.ground_raven_group.add(new_ground_raven)
            self.all_enemies.add(new_ground_raven)

    def spawn_deadly_raven(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_deadly_raven_spawn_time > self.deadly_raven_spawn:
            self.last_deadly_raven_spawn_time = current_time
            new_deadly_raven = DeadlyFlyRaven()
            self.deadly_raven_group.add(new_deadly_raven)
            self.all_enemies.add(new_deadly_raven)

    def fl_rav_spawn_rate(self, from_, to_):
        self.fly_raven_spawn = randint(from_, to_)

    def gr_rav_spawn_rate(self, from_, to_):
        self.ground_raven_spawn = randint(from_, to_)

    def deadly_fl_rav_spawn_rate(self, from_, to_):
        self.deadly_raven_spawn = randint(from_, to_)

    def level_one(self):

        """Level settings:"""
        self.ground_raven_hp = 100
        self.collisions.fly_raven_damage = 30
        self.collisions.ground_raven_damage = 25

        self.gr_rav_spawn_rate(1300, 2100)
        self.fl_rav_spawn_rate(1000, 2000)
        self.deadly_fl_rav_spawn_rate(4000, 15000)
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

        self.gr_rav_spawn_rate(1200, 2100)
        self.fl_rav_spawn_rate(1000, 1200)
        self.deadly_fl_rav_spawn_rate(3000, 15000)
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
