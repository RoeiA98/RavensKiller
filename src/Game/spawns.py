from src.Sprites.Enemies.deadly_fly_ravens import DeadlyFlyRaven
from src.Sprites.Enemies.fly_ravens import FlyRaven
from src.Sprites.Enemies.ground_ravens import GroundRaven


class Spawns:
    def __init__(self, fly_raven_group, ground_raven_group, deadly_raven_group, all_enemies, game_screen):

        # General
        self.all_enemies = all_enemies
        self.game_screen = game_screen
        self.elapsed_time = 0

        # Fly Ravens
        self.fly_raven_group = fly_raven_group
        self.fly_raven_spawn = 0
        self.last_fly_raven_spawn_time = 0

        # Ground Ravens
        self.ground_raven_group = ground_raven_group
        self.ground_raven_spawn = 0
        self.last_ground_raven_spawn_time = 0
        self.ground_raven_hp = 0

        # Deadly Ravens
        self.deadly_raven_group = deadly_raven_group
        self.deadly_raven_spawn = 0
        self.last_deadly_raven_spawn_time = 0

    def reset_all_last_spawns(self):
        self.last_fly_raven_spawn_time = 0
        self.last_ground_raven_spawn_time = 0
        self.last_deadly_raven_spawn_time = 0

    def spawn_enemy(self, spawn_interval, last_spawn_time_attr, enemy_class, group, *args, **kwargs):
        if spawn_interval:
            if (self.elapsed_time - getattr(self, last_spawn_time_attr) > spawn_interval):
                setattr(self, last_spawn_time_attr, self.elapsed_time)
                new_enemy = enemy_class(*args, **kwargs)
                group.add(new_enemy)
                self.all_enemies.add(new_enemy)

    def spawn_fly_raven(self):
        self.spawn_enemy(self.fly_raven_spawn, 'last_fly_raven_spawn_time', FlyRaven, self.fly_raven_group)

    def spawn_ground_raven(self):
        self.spawn_enemy(self.ground_raven_spawn, 'last_ground_raven_spawn_time', GroundRaven, self.ground_raven_group, self.ground_raven_hp, screen=self.game_screen)

    def spawn_deadly_raven(self):
        self.spawn_enemy(self.deadly_raven_spawn, 'last_deadly_raven_spawn_time', DeadlyFlyRaven, self.deadly_raven_group)