import pygame
from datetime import timedelta

class GameTimer:
    def __init__(self):
        self.start_time = 0
        self.paused_time = 0
        self.last_pause_time = 0
        self.is_paused = False
        self.is_running = False
    
    def start(self):
        self.start_time = pygame.time.get_ticks()
        self.is_running = True
        self.is_paused = False
        self.paused_time = 0
    
    def pause(self):
        if self.is_running and not self.is_paused:
            self.last_pause_time = pygame.time.get_ticks()
            self.is_paused = True
    
    def resume(self):
        if self.is_paused:
            self.paused_time += pygame.time.get_ticks() - self.last_pause_time
            self.is_paused = False
    
    def reset(self):
        self.start_time = pygame.time.get_ticks()
        self.paused_time = 0
        self.last_pause_time = 0
        self.is_paused = False
        self.is_running = False
    
    def get_elapsed_time_ms(self):
        if not self.is_running:
            return 0
        current_pause_time = self.paused_time
        if self.is_paused:
            current_pause_time += pygame.time.get_ticks() - self.last_pause_time
        return pygame.time.get_ticks() - self.start_time - current_pause_time
    
    def get_elapsed_time(self):
        return timedelta(milliseconds=self.get_elapsed_time_ms())