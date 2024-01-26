import pygame as pg
from math import ceil


class Bar:
    def __init__(self, coordinates, size, img, value=3):
        self.coordinates = coordinates
        self.size = size
        self.fill_value = value
        self.special_state = 0
        self.bar_img = "assets/" + img + "0.png"
        self.void_bar = pg.image.load('assets/void_bar.png').convert_alpha()
        self.color_bar = pg.image.load("assets/bar_lvl_" + str(round(value)) + ".png").convert_alpha()

    def display(self, screen):
        bar = pg.image.load(self.bar_img).convert_alpha()
        screen.blit(bar, (self.coordinates[0], self.coordinates[1]))
        pg.display.flip()

        self.update(screen, (self.fill_value, self.special_state))
        print("bar created")

    def update(self, screen, args=(None, -1)):
        if args[0]:
            self.update_values(args[0])
        if args[1] != -1:
            self.update_state(args[1], screen)
        self.update_on_screen(screen)
        print("bar updated")

    def update_values(self, value):
        self.fill_value = value
        self.color_bar = pg.image.load("assets/bar_lvl_" + str(3 if ceil(value) > 3 else ceil(value)) + ".png").convert_alpha()

    def update_state(self, state, screen):
        self.bar_img = self.bar_img.replace(str(self.special_state)+'.png', str(state) + '.png')
        self.special_state = state

    def update_on_screen(self, screen):
        cropped_region = (1, 1, (self.fill_value / 3 * 120), 32)

        screen.blit(self.void_bar, (self.coordinates[0] - 1, self.coordinates[1] - 1))
        screen.blit(self.color_bar, (self.coordinates[0], self.coordinates[1]), cropped_region)
        pg.display.flip()
