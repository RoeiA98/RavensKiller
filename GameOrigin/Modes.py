from GameOrigin.Game import *
from UI.GameScenes import *
from Sprites.Player import *
from GameOrigin.Spawns import *
from sys import exit
from UI.Score import *


class GameModes(Game):

    def __init__(self):
        super().__init__()

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
        self.game_current_level_scene.level_score = 0
        self.ground_ravens_kills = 0
        self.fly_ravens_kills = 0
        self.game_current_level_scene.fl_kills = 0
        self.game_current_level_scene.gr_kills = 0

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
        self.game_current_level_scene.level_score = 0
        self.ground_ravens_kills = 0
        self.fly_ravens_kills = 0
        self.game_current_level_scene.fl_kills = 0
        self.game_current_level_scene.gr_kills = 0
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
            self.game_current_level_scene.update(self.game_screen)
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
