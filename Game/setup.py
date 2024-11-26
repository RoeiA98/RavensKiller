from Game.spawns import *
from SpritesLogic.collision import CollisionsHandler
from UI.GameScenes import GameScenes
from UI.health import PlayerHealth
from UI.score import Score
from UI.FPS import FPS


class Game(pygame.sprite.Sprite):

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
        self.fps = FPS()
        self.levels = []
        self.game_level_scenes = [None]

        """ ------------------------------------------------- """

        """ Game Attributes """
        self.active_game_score = 0
        self.ground_ravens_kills = 0
        self.fly_ravens_kills = 0
        self.display_player_score = Score(self.active_game_score)
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
                
        self.keys = pygame.key.get_pressed()
        self.game_font = pygame.font.Font('Fonts/Amatic-Bold.ttf', 40)
        self.level_text = None
        self.objective_text = None
        self.objective_text_rect = None
        self.progress_text = None
        self.progress_text_rect = None
        self.level_text_rect = None
        self.objective2_text = None
        self.objective2_text_rect = None

        """" ------------------------------------------------- """

        """ Player Attributes """
        self.player = pygame.sprite.GroupSingle()
        self.player_health = PlayerHealth(100, 100)
        self.bullet = pygame.sprite.Group()

        """" ------------------------------------------------- """

        """ Initializers """
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
