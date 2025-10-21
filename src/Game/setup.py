import pygame
from src.Game.spawns import *
from src.Sprites.collision import CollisionsHandler
from UI.GameScenes import GameScenes
from UI.GameIntro import GameIntro
from UI.PlayerHealth import PlayerHealth
from UI.GameScore import GameScore
from UI.FPS import FPS
from UI.Timer import Timer
from src.Sprites.player import Player


class Game(pygame.sprite.Sprite):

    def __init__(self):
        """General Attributes"""
        self.MAX_FPS = 60
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1000, 550
        self.game_screen = pygame.display.set_mode(
            (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        )
        self.game_font = pygame.font.Font("fonts/Amatic-Bold.ttf", 40)
        self.image = pygame.image.load("assets/gameBG3.png").convert()

        """ ------------------------------------------------- """

        """ Draw UI """
        self.fps = FPS()
        self.timer = Timer()
        self.player_health = PlayerHealth()
        self.game_score = GameScore()

        """ ------------------------------------------------- """

        """ Enemy Attributes """
        self.all_enemies = pygame.sprite.Group()
        self.fly_raven_group = pygame.sprite.Group()
        self.ground_raven_group = pygame.sprite.Group()
        self.deadly_raven_group = pygame.sprite.Group()

        """" ------------------------------------------------- """

        """ Scenes Attributes """
        self.game_scenes = GameScenes()
        self.game_intro = GameIntro()

        """" ------------------------------------------------- """

        """ Player Attributes """
        self.player = pygame.sprite.GroupSingle()
        self.player.add(Player())
        self.bullet = pygame.sprite.Group()

        """" ------------------------------------------------- """

        """ Initializers """
        self.collisions = CollisionsHandler(
            self.player,
            self.player_health,
            self.fly_raven_group,
            self.ground_raven_group,
            self.deadly_raven_group,
            self.all_enemies,
        )

        self.spawns = Spawns(
            self.fly_raven_group,
            self.ground_raven_group,
            self.deadly_raven_group,
            self.all_enemies,
            self.game_screen,
        )
