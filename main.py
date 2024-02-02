"""

Main function

"""
import pygame
from src.game import Game


def main():
    """

    Prenez bien soin de Nico, la petite pousse miconide

    """
    game = Game()
    game.update_screen()
    running = True

    while running:
        running = game.check_event()

    pygame.quit()


if __name__ == '__main__':
    main()
