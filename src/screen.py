import pygame as pg
from src.button import Button


class Screen:
    def __init__(self):
        self.current_w = 480
        self.current_h = 270
        self.screen = None

        self.create_window()

    def create_window(self):
        pg.init()
        pg.display.set_caption("Nico la jeune pousse myconide")
        pg.display.set_icon(pg.image.load("assets/nico_icon.png"))

        self.screen = pg.display.set_mode((self.current_w, self.current_h))

    def display_screen(self, items):
        self.screen.fill("#181425FF")

        for item in items:
            for element in item:
                item[element].display(self.screen)
                print(f"displayed : {element}")

    def update_item(self, item, *args):
        if not args:
            item.update(self.screen)
        else:
            item.update(self.screen, args)
