from src.game import Game

def main():
    game = Game()
    game.update_screen()
    running = True

    while running:
        running = game.check_event()


if __name__ == '__main__':
    main()
