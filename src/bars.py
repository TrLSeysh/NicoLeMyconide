import pygame as pg
from math import ceil
from src.item import Item


class Bar(Item):
    def __init__(self, coordinates, size, img, value=3):
        """

        Class is used for creating bar item, for loading or stats

        :param coordinates: location on the screen of the bar item
        :param size: the size of bar item
        :param img: the image of bar item
        :param value: maximum value for the bar item
        """
        super().__init__(coordinates, size)

        self.fill_value = value
        self.special_state = 0
        self.bar_img = "assets/" + img + "0.png"
        self.color_bar = pg.image.load("assets/bar_lvl_" + str(round(value)) + ".png").convert_alpha()

    def display(self, screen):
        """

        Display the bar item on the screen

        :param screen: the pygame.screen element for the game
        """
        bar = pg.image.load(self.bar_img).convert_alpha()
        screen.blit(bar, self.coordinates)
        pg.display.flip()

        self.update(screen, (self.fill_value, self.special_state))

    def update(self, screen, args=(None, -1)):
        """

        Update the bar item on the screen

        :param screen: the pygame.screen element for the game
        :param args: used to update state, value or both (state change bar visual, value change visual pourcentage)
        """
        if args[0]:
            self.update_values(args[0])
        if args[1] != -1:
            self.update_state(args[1])
        self.update_on_screen(screen)

    def update_values(self, value):
        """

        Update bar value to passed value

        :param value: the new bar value
        """
        self.fill_value = value
        self.color_bar = pg.image.load("assets/bar_lvl_" + str(3 if ceil(value) > 3 else (1 if ceil(value) < 1 else ceil(value))) + ".png").convert_alpha()

    def update_state(self, state):
        """

        Update bar state to passed state (e.g change lightning to moon for energy)

        :param state: new bar state
        """
        self.bar_img = self.bar_img.replace(str(self.special_state)+'.png', str(state) + '.png')
        self.special_state = state

    def update_on_screen(self, screen):
        """

        Update bar on the screen

        :param screen: the pygame.screen element for the game
        """
        cropped_region = (1, 1, (self.fill_value / 3 * 120), 32)

        screen.blit(self.color_bar, self.coordinates, cropped_region)

        bar = pg.image.load(self.bar_img).convert_alpha()
        screen.blit(bar, self.coordinates)
        pg.display.flip()
