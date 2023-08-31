import asyncio
import pygame

from LevelsDesign.GameLevels import GameLevels


# async def main():
#
#     game = GameLevels()
#     fps = FPS()
#
#     while game.game_running:
#         if game.game_active_status:
#             game.levels_handler()
#
#         else:
#             # End game and reset levels
#             game.game_over()
#             game.game_restart()
#
#         fps.render(game.game_screen)
#         pygame.display.update()
#         fps.clock.tick(60)
#         await asyncio.sleep(0)


if __name__ == "__main__":
    pygame.init()
    game = GameLevels()
    asyncio.run(game.run_game())
