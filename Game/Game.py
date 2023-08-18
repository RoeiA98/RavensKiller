import pygame

from Sprites.Collision import CollisionsHandler
from Sprites.Player import Player
from Sprites.Scenes import GameScenes
from Sprites.Spawns import Spawns
from UI.Health import PlayerHealth
from UI.Levels import *
from UI.Score import Score


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

        """" ------------------------------------------------- """

        """ Scenes Attributes """
        self.levels_manager = 1
        self.game_scenes = GameScenes()
        self.game_levels = [  # level correlates with index
            None,
            LevelOne(self.active_game_score),
            LevelTwo(self.active_game_score)
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

        self.spawns = Spawns(self.fly_raven_group,
                             self.ground_raven_group,
                             self.deadly_raven_group,
                             self.all_enemies,
                             self.game_screen)
