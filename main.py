"""

Main function

"""
import pygame
from src.game import Game


def main():
    """

    Take care of Nico, he is cute and must be protected

    """
    game = Game()
    game.update_screen()
    running = True

    while running:
        running = game.check_event()

    pygame.quit()


if __name__ == '__main__':
    main()
