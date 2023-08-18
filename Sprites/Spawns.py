import pygame
from Sprites.Enemies import *


def set_spawn_rate(from_, to_):
    return randint(from_, to_)


class Spawns:

    def __init__(self,
                 fly_raven_group,
                 ground_raven_group,
                 deadly_raven_group,
                 all_enemies,
                 game_screen):

        self.fly_raven_group = fly_raven_group
        self.ground_raven_group = ground_raven_group
        self.deadly_raven_group = deadly_raven_group
        self.all_enemies = all_enemies
        self.fly_raven_spawn = 0
        self.ground_raven_spawn = 0
        self.deadly_raven_spawn = 0
        self.last_ground_raven_spawn_time = 0
        self.last_fly_raven_spawn_time = 0
        self.last_deadly_raven_spawn_time = 0
        self.game_screen = game_screen

    def spawn_fly_raven(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_fly_raven_spawn_time > self.fly_raven_spawn:
            self.last_fly_raven_spawn_time = current_time
            new_fly_raven = FlyRaven()
            self.fly_raven_group.add(new_fly_raven)
            self.all_enemies.add(new_fly_raven)

    def spawn_ground_raven(self, ground_raven_hp):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_ground_raven_spawn_time > self.ground_raven_spawn:
            self.last_ground_raven_spawn_time = current_time
            new_ground_raven = GroundRaven(ground_raven_hp, self.game_screen)
            self.ground_raven_group.add(new_ground_raven)
            self.all_enemies.add(new_ground_raven)

    def spawn_deadly_raven(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_deadly_raven_spawn_time > self.deadly_raven_spawn:
            self.last_deadly_raven_spawn_time = current_time
            new_deadly_raven = DeadlyFlyRaven()
            self.deadly_raven_group.add(new_deadly_raven)
            self.all_enemies.add(new_deadly_raven)
