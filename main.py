import pygame

from LevelsDesign.GameLevels import GameLevels


def main():

    game = GameLevels()

    while game.game_running:
        if game.game_active_status:
            game.levels_handler()
        else:
            # End game and reset levels
            game.game_over()
            game.game_restart()

        pygame.display.update()
        game.clock.tick(game.MAX_FPS)  # MAX 60 FPS


if __name__ == "__main__":

    pygame.init()
    main()
