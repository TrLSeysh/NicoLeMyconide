import pygame as pg


class Button:
    def __init__(self, coordinates, size, img):
        self.coordinates = coordinates
        self.size = size
        self.is_pressed = False
        self.button_img = pg.image.load("assets/" + img + ".png").convert_alpha()
        self.pressed_img = pg.image.load("assets/" + img + "_pressed.png").convert_alpha()

    def display(self, screen):
        screen.blit(self.button_img, self.coordinates)
        pg.display.flip()

    def update(self, screen):
        self.is_pressed = not self.is_pressed

        screen.blit(self.pressed_img if self.is_pressed else self.button_img, self.coordinates)
        pg.display.flip()
