import pygame as pg
class Game:
    def __init__(self):
        self.current_w = 480
        self.current_h = 270

        self.create_window()

    def create_window(self):
        pg.init()
        pg.display.set_caption("Nico la jeune pousse myconide")
        pg.display.set_icon(pg.image.load("assets/nico_icon.png"))
        pg.display.set_mode((self.current_w, self.current_h))

    def display_main_menu(self):
        pass
    def display_game(self):
        pass
    def display_element(self):
        pass
