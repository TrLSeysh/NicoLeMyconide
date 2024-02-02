import pygame as pg
from src.item import Item


class Food(Item):
    def __init__(self, coordinates, size, name, food_regen=5, state=2):
        super().__init__(coordinates, size)

        self.name = name
        self.state = state
        self.food_regen = food_regen
        self.closed_img = pg.image.load("assets/cardbox.png").convert_alpha()
        self.opened_img = pg.image.load("assets/" + name + ".png").convert_alpha()

    def display(self, screen):
        print(self.state)
        if self.state == 2:
            screen.blit(self.closed_img, self.coordinates)
            pg.display.flip()
        elif self.state == 1:
            screen.blit(self.opened_img, (self.coordinates[0] + 16, self.coordinates[1] + 16))
            pg.display.flip()

    def update(self, screen, args=None):
        if self.state == 2:
            self.state -= 1
            self.display(screen)
        elif self.state == 1:
            self.state -= 1
