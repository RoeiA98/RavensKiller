import pygame

from SpritesLogic.Enemies.DeadlyFlyRavens import DeadlyFlyRaven
from SpritesLogic.Enemies.FlyRavens import FlyRaven
from SpritesLogic.Enemies.GroundRavens import GroundRaven
from SpritesLogic.enemy import *


def set_spawn_rate(from_, to_):
    return randint(from_, to_)


class Spawns:

    def __init__(self,
                 fly_raven_group,
                 ground_raven_group,
                 deadly_raven_group,
                 all_enemies,
                 game_screen):

        # Fly Ravens
        self.fly_raven_group = fly_raven_group
        self.fly_raven_spawn = 0
        self.last_fly_raven_spawn_time = 0

        # Ground Ravens
        self.ground_raven_group = ground_raven_group
        self.ground_raven_spawn = 0
        self.last_ground_raven_spawn_time = 0

        # Deadly Ravens
        self.deadly_raven_group = deadly_raven_group
        self.deadly_raven_spawn = 0
        self.last_deadly_raven_spawn_time = 0

        # General
        self.all_enemies = all_enemies
        self.game_screen = game_screen

    def spawn_fly_raven(self):
        current_time = pygame.time.get_ticks()

        if self.fly_raven_spawn:
            if current_time - self.last_fly_raven_spawn_time > self.fly_raven_spawn:
                self.last_fly_raven_spawn_time = current_time
                new_fly_raven = FlyRaven()
                self.fly_raven_group.add(new_fly_raven)
                self.all_enemies.add(new_fly_raven)

    def spawn_ground_raven(self, ground_raven_hp):
        current_time = pygame.time.get_ticks()

        if self.ground_raven_spawn:
            if current_time - self.last_ground_raven_spawn_time > self.ground_raven_spawn:
                self.last_ground_raven_spawn_time = current_time
                new_ground_raven = GroundRaven(ground_raven_hp, self.game_screen)
                self.ground_raven_group.add(new_ground_raven)
                self.all_enemies.add(new_ground_raven)

    def spawn_deadly_raven(self):
        current_time = pygame.time.get_ticks()

        if self.deadly_raven_spawn:
            if current_time - self.last_deadly_raven_spawn_time > self.deadly_raven_spawn:
                self.last_deadly_raven_spawn_time = current_time
                new_deadly_raven = DeadlyFlyRaven()
                self.deadly_raven_group.add(new_deadly_raven)
                self.all_enemies.add(new_deadly_raven)
