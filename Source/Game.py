import pygame
from UI import Levels
from Sprites.Scences import *
from Sprites.Enemies import *
from Sprites.Player import *
from sys import exit
from UI.Score import *


class Game:
    def __init__(self):
        self.MAX_FPS = 60
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1000, 550
        self.clock = pygame.time.Clock()
        self.game_active_status = False
        self.game_intro_status = True
        self.active_game_score = 0
        self.enemy_spawn_timer = pygame.USEREVENT + 1
        self.levels_manager = 1
        self.continue_screen = False
        self.game_running = True

        self.game_scenes = GameScenes()
        self.game_levels = [
            Levels.LevelOne(self.active_game_score),
            Levels.LevelTwo(self.active_game_score)
        ]
        self.game_screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        # Groups
        #   Player:
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.player_health = PlayerHealth(100, 100)
        self.display_player_score = Score(self.active_game_score)
        #   Enemies:
        self.enemy_group = pygame.sprite.Group()
        self.fly_raven_group = pygame.sprite.Group()
        self.ground_raven_group = pygame.sprite.Group()
        #   Bullet
        self.bullet = pygame.sprite.Group()

    def events_handler(self, spawn_rate_a, spawn_rate_b):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if self.game_active_status:

                self.enemy_spawn_rate(spawn_rate_a, spawn_rate_b)

                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.bullet.add(Player().shoot_bullet(self.player.sprite.rect.x,
                                                          self.player.sprite.rect.y,
                                                          self.player.sprite.player_current_direction))

                # spawning enemies
                if event.type == self.enemy_spawn_timer:
                    # randomly spawning enemies with random directions
                    if randint(0, 2):
                        self.fly_raven_group.add(FlyRaven())
                        self.enemy_group.add(self.fly_raven_group)
                    else:
                        self.ground_raven_group.add(GroundRaven())
                        self.enemy_group.add(self.ground_raven_group)
            else:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    self.game_reset()
                    self.game_active_status = True

    def game_run(self):

        self.game_intro()

        while self.game_running:

            self.events_handler(200, 350)

            if self.game_active_status:
                # level logic
                if self.levels_manager == 1:
                    self.level_one()

                if self.levels_manager == 2:
                    self.level_two()

            else:
                # End game and reset levels
                self.game_over()
                self.levels_manager = 1

            pygame.display.update()
            self.clock.tick(self.MAX_FPS)  # MAX 60 FPS

    def game_intro(self):
        while self.game_intro_status:

            self.game_scenes.game_welcome()
            pygame.display.update()

            for intro_event in pygame.event.get():
                if intro_event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if intro_event.type == pygame.KEYDOWN and intro_event.key == pygame.K_SPACE:
                    self.game_intro_status = False

        self.game_active_status = True

    def game_continue(self):
        self.fly_raven_group.empty()
        self.ground_raven_group.empty()
        self.player.sprite.rect = self.player.sprite.image.get_rect(midbottom=(500, 450))

        while self.continue_screen:
            self.game_scenes.next_level()
            pygame.display.update()

            for intro_event in pygame.event.get():
                if intro_event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if intro_event.type == pygame.KEYDOWN and intro_event.key == pygame.K_SPACE:
                    self.continue_screen = False

        self.game_active_status = True

    def game_reset(self):
        self.player_health.hp = 100
        self.display_player_score.current_score = 0
        self.game_active_status = True

    def game_over(self):
        # Deleting enemies
        self.fly_raven_group.empty()
        self.ground_raven_group.empty()
        # Resetting player position
        self.player.sprite.rect = self.player.sprite.image.get_rect(midbottom=(500, 450))
        # Game over scene
        self.game_scenes.game_over(self.display_player_score.current_score)
        self.game_active_status = False

    def game_active(self):
        # Start game
        self.game_scenes.game_active()

        # Score
        self.display_player_score.update(self.game_screen)

        # Player
        self.player.draw(self.game_screen)
        self.player.update()

        # Player health
        self.player_health.draw(self.game_screen)
        self.player_health.draw_hp_text(self.game_screen)

        # Enemy
        self.fly_raven_group.update()
        self.fly_raven_group.draw(self.game_screen)

        self.ground_raven_group.update()
        self.ground_raven_group.draw(self.game_screen)

        # Bullet
        self.bullet.draw(self.game_screen)
        self.bullet.update()

        # Collision
        # bullet_collision()
        self.game_active_status = self.player_collision()
        # game_active = True  # for testings without collision

    def enemy_spawn_rate(self, from_, to_):
        pygame.time.set_timer(self.enemy_spawn_timer, randint(from_, to_))

    def bullet_collision(self):
        if pygame.sprite.groupcollide(self.bullet, self.ground_raven_group, True, True):
            self.display_player_score.current_score += 1
        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1

    def player_collision(self):

        if pygame.sprite.spritecollide(self.player.sprite, self.fly_raven_group, True):
            self.player_health.hp -= 30
            if self.player_health.hp <= 0:
                self.enemy_group.empty()
                return False

        if pygame.sprite.spritecollide(self.player.sprite, self.ground_raven_group, True):
            self.player_health.hp -= 25
            if self.player_health.hp <= 0:
                self.enemy_group.empty()
                return False

        return True

    def level_one(self):
        self.game_active()
        self.game_levels[0].display_level()

        if pygame.sprite.groupcollide(self.bullet, self.ground_raven_group, True, True):
            self.display_player_score.current_score += 1
            self.game_levels[0].level_score += 1
            if self.game_levels[0].level_score == 5:
                self.levels_manager = 2
                self.continue_screen = True
                self.game_continue()
                self.game_reset()
                return False
        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1

        self.game_levels[0].update(self.game_screen)

    def level_two(self):
        self.game_active()
        self.game_levels[1].display_level()

        if pygame.sprite.groupcollide(self.bullet, self.ground_raven_group, True, True):
            self.display_player_score.current_score += 1
            self.game_levels[1].level_score += 1
            if self.game_levels[1].level_score == 15:
                self.levels_manager = 2
                self.continue_screen = True
                self.game_continue()
                self.game_reset()
                return False
        if pygame.sprite.groupcollide(self.bullet, self.fly_raven_group, True, True):
            self.display_player_score.current_score += 1

        self.game_levels[1].update(self.game_screen)
