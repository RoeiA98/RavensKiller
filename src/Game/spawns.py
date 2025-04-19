from src.Sprites.Enemies.DeadlyFlyRavens import DeadlyFlyRaven
from src.Sprites.Enemies.FlyRavens import FlyRaven
from src.Sprites.Enemies.GroundRavens import GroundRaven


class Spawns:

    def __init__(
        self,
        fly_raven_group,
        ground_raven_group,
        deadly_raven_group,
        all_enemies,
        game_screen,
    ):

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

    def spawn_fly_raven(self):
        if self.fly_raven_spawn:
            if (
                self.elapsed_time - self.last_fly_raven_spawn_time
                > self.fly_raven_spawn
            ):
                self.last_fly_raven_spawn_time = self.elapsed_time
                new_fly_raven = FlyRaven()
                self.fly_raven_group.add(new_fly_raven)
                self.all_enemies.add(new_fly_raven)

    def spawn_ground_raven(self):
        if self.ground_raven_spawn:
            if (
                self.elapsed_time - self.last_ground_raven_spawn_time
                > self.ground_raven_spawn
            ):
                self.last_ground_raven_spawn_time = self.elapsed_time
                new_ground_raven = GroundRaven(
                    self.ground_raven_hp, screen=self.game_screen
                )
                self.ground_raven_group.add(new_ground_raven)
                self.all_enemies.add(new_ground_raven)

    def spawn_deadly_raven(self):
        if self.deadly_raven_spawn:
            if (
                self.elapsed_time - self.last_deadly_raven_spawn_time
                > self.deadly_raven_spawn
            ):
                self.last_deadly_raven_spawn_time = self.elapsed_time
                new_deadly_raven = DeadlyFlyRaven()
                self.deadly_raven_group.add(new_deadly_raven)
                self.all_enemies.add(new_deadly_raven)
