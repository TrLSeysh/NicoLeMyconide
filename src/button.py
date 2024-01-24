import pygame as pg


class Button:
    def __init__(self, x, y, size_x, size_y, img, screen):
        self.x = x
        self.y = y
        self.size_x = size_x
        self.size_y = size_y
        self.is_pressed = False
        self.button_img = pg.image.load("assets/" + img + ".png").convert()
        self.pressed_img = pg.image.load("assets/" + img + "_pressed.png").convert()

    def display(self, screen):
        screen.blit(self.button_img, (self.x, self.y))
        pg.display.flip()
        print("button created")

    def update(self, screen):
        self.is_pressed = not self.is_pressed
        screen.blit(self.pressed_img if self.is_pressed else self.button_img, (self.x, self.y))
        pg.display.flip()

        print("button updated")
