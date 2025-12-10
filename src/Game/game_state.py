from enum import Enum

class GameState(Enum):
    INTRO = "intro"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    NEXT_LEVEL = "next_level"
    FINAL_SCREEN = "final_screen"
    DISPLAY_OBJECTIVE = "display_objective"

class GameStateManager:
    def __init__(self):
        self._current_state = GameState.INTRO
        self._previous_state = None
    
    @property
    def current_state(self):
        return self._current_state
    
    @property
    def previous_state(self):
        return self._previous_state
    
    def change_state(self, new_state):
        if new_state != self._current_state:
            self._previous_state = self._current_state
            self._current_state = new_state
    
    def is_state(self, state):
        return self._current_state == state
    
    def is_any_state(self, *states):
        return self._current_state in states