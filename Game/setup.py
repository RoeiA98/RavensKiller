from Game.spawns import *
from SpritesLogic.collision import CollisionsHandler
from UI.GameScenes import GameScenes
from UI.LevelScenes import Level1Scene, Level2Scene, Level3Scene, Level4Scene
from UI.health import PlayerHealth
from UI.levels import *
from UI.score import Score


class Game:

    def __init__(self):

        """ General Attributes """
        self.MAX_FPS = 60
        self.SCREEN_WIDTH, self.SCREEN_HEIGHT = 1000, 550
        self.game_screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.game_active_status = False
        self.game_intro_status = True
        self.continue_screen = False
        self.game_running = False
        self.final_level = False

        """ ------------------------------------------------- """

        """ Game Attributes """
        self.active_game_score = 0
        self.ground_ravens_kills = 0
        self.fly_ravens_kills = 0
        self.display_player_score = Score(self.active_game_score)

        # pause experiment
        self.game_pause = False

        """ ------------------------------------------------- """

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
            # Level1.LevelOne(self.active_game_score, self.ground_ravens_kills),
            Level1Scene.LevelOneScene(self.active_game_score, self.ground_ravens_kills),
            Level2Scene.LevelTwoScene(self.active_game_score, self.ground_ravens_kills),
            Level3Scene.LevelThreeScene(self.active_game_score, self.ground_ravens_kills, self.fly_ravens_kills),
            Level4Scene.LevelFourScene(self.active_game_score, self.fly_ravens_kills)
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
