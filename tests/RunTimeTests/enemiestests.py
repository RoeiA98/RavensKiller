import sys
import os

# Change the working directory to the root directory of the project
os.chdir(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
# Add the root directory to the Python path
sys.path.append(os.getcwd())
import pygame
import asyncio
from src.Game.handler import Handler


class EnemiesTests(Handler):

    def __init__(self):
        super().__init__()
        self.font = pygame.font.SysFont("Verdana", 20)

    def display_active_enemies(self):
        active_dr = self.game_font.render(
            f"Deadly Ravens: {len(self.deadly_raven_group)}", True, "Black"
        ).convert_alpha()
        active_gr = self.game_font.render(
            f"Ground Ravens: {len(self.ground_raven_group)}", True, "Black"
        ).convert_alpha()
        active_fr = self.game_font.render(
            f"Fly Ravens: {len(self.fly_raven_group)}", True, "Black"
        ).convert_alpha()
        all_enemies = self.game_font.render(
            f"Overall enemies: {len(self.all_enemies)}", True, "Black"
        ).convert_alpha()
        self.game_screen.blit(active_dr, (200, 30))
        self.game_screen.blit(active_gr, (200, 80))
        self.game_screen.blit(active_fr, (200, 130))
        self.game_screen.blit(all_enemies, (200, 180))

    def print_current_enemies(self):
        print(f"current level: {self.current_level}")
        # Deadly ravens
        print(f"\nActive Deadly Ravens: {len(self.deadly_raven_group)}")
        print(f"Active Deadly Ravens Spawn Time: {self.spawns.deadly_raven_spawn}")
        print(
            f"Active Deadly Ravens Last Spawn Time: {self.spawns.last_deadly_raven_spawn_time}"
        )
        # Ground ravens
        print(f"\nActive Ground Ravens: {len(self.ground_raven_group)}")
        print(f"Active Deadly Ravens Spawn Time: {self.spawns.ground_raven_spawn}")
        print(
            f"Active Deadly Ravens Last Spawn Time: {self.spawns.last_ground_raven_spawn_time}"
        )
        # Fly ravens
        print(f"\nActive Fly Ravens: {len(self.fly_raven_group)}")
        print(f"Active Deadly Ravens Spawn Time: {self.spawns.fly_raven_spawn}")
        print(
            f"Active Deadly Ravens Last Spawn Time: {self.spawns.last_fly_raven_spawn_time}"
        )
        print("-------------------------------------------")
        # ground_raven_count = sum(1 for enemy in self.all_enemies.sprites() if isinstance(enemy, GroundRaven))

    async def run_game(self):
        while True:
            while not self.game_running:
                self.game_intro.intro_screen_menu()
                self.game_running = self.game_intro.handle_game_intro_events()
                pygame.display.update()
                await asyncio.sleep(0)

            self.game_active_status = True
            self.start_time = pygame.time.get_ticks()

            while self.game_running:
                if self.game_active_status:
                    self.game_handler()
                    self.print_current_enemies()
                else:
                    self.game_stop()

                pygame.display.update()
                self.fps.clock.tick(self.MAX_FPS)
                await asyncio.sleep(0)


async def main():
    pygame.init()
    enemies_test = EnemiesTests()

    await enemies_test.run_game()


if __name__ == "__main__":
    asyncio.run(main())
