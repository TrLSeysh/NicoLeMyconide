from src.game import Game
import pygame


def main():
    game = Game()
    game.update_screen()
    running = True

    while running:
        running = game.check_event()

    pygame.quit()


if __name__ == '__main__':
    main()
