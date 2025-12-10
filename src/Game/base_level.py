from src.Game.game import Game


class BaseLevel(Game):
    def __init__(self):
        super().__init__()

    def load_settings(self):
        pass

    def play(self):
        pass

    def display_objective(self, screen):
        pass

    def display_level(self, screen):
        pass