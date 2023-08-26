from GameOrigin.Spawns import *
from Sprites.Collision import CollisionsHandler
from UI.GameScenes import GameScenes
from UI.LevelScenes import Level1Scene, Level2Scene, Level3Scene
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

        """ GameOrigin Attributes """
        self.active_game_score = 0
        self.ground_raven_kills = 0
        self.fly_ravens_kills = 0
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
        self.current_level = 1
        self.game_scenes = GameScenes()
        self.game_level_scenes = [  # level correlates with index
            None,
            Level1Scene.LevelOneScene(self.active_game_score),
            Level2Scene.LevelTwoScene(self.active_game_score),
            Level3Scene.LevelThreeScene(self.active_game_score,
                                        self.ground_raven_kills,
                                        self.fly_ravens_kills)
        ]
        self.game_current_level_scene = self.game_level_scenes[self.current_level]

        """" ------------------------------------------------- """

        """ Player Attributes """
        self.player = pygame.sprite.GroupSingle()
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
