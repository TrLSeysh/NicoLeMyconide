"""

Screen is parameters and functions linked

"""
import pygame as pg


class Screen:
    def __init__(self):
        self.current_w = 480
        self.current_h = 270
        self.screen = None
        self.home_background = None
        self.main_background = None
        self.menu_background = None
        self.current_background = None

        self.create_window()

    def create_window(self):
        pg.init()
        pg.display.set_caption("Nico la jeune pousse myconide")
        pg.display.set_icon(pg.image.load("assets/nico_icon.png"))

        self.screen = pg.display.set_mode((self.current_w, self.current_h))
        self.home_background = pg.image.load("assets/home_background.png")
        self.main_background = pg.image.load("assets/main_background.png")
        self.menu_background = pg.image.load("assets/menu_background.png")

    def display_background(self, name):
        if name == "home":
            self.screen.blit(self.home_background, (0, 0))
            self.current_background = self.home_background
        elif name == "main":
            self.screen.blit(self.main_background, (0, 0))
            self.current_background = self.main_background
        elif name == "menu":
            self.screen.blit(self.menu_background, (0, 0))
            self.current_background = self.menu_background

    def display_screen(self, items):
        for item in items:
            for element in item:
                item[element].display(self.screen)

    def update_item(self, item, *args):
        self.screen.blit(self.current_background, item.coordinates, (item.coordinates, item.size))

        if not args:
            item.update(self.screen)
        else:
            item.update(self.screen, args)

    def display_anim(self, coordinates, size, state, img):
        self.screen.blit(self.current_background, coordinates, (coordinates, size))

        if state:
            anim_img = pg.image.load("assets/" + img + str(state) + ".png").convert_alpha()
            self.screen.blit(anim_img, coordinates)

        pg.display.update()

    def remove_element_from_screen(self, coordinates, size):
        self.screen.blit(self.current_background, coordinates, (coordinates, size))
