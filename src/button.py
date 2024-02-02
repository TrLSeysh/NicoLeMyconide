"""

Button class used to change menu and general interaction

"""

import pygame as pg
from src.item import Item


class Button(Item):
    """

    Class is used for creating button item, for changing menu or interact with the game

    :param coordinates: location on the screen of the bar item
    :param size: the size of button item
    :param img: the image of button item
    """
    def __init__(self, coordinates: list, size: list, img: str) -> None:
        super().__init__(coordinates, size)

        self.is_pressed = False
        self.button_img = pg.image.load("assets/" + img + ".png").convert_alpha()
        self.pressed_img = pg.image.load("assets/" + img + "_pressed.png").convert_alpha()

    def display(self, screen: pg.display) -> None:
        """

        Display the button item on the screen

        :param screen: the pygame.display element for the game
        """
        screen.blit(self.button_img, self.coordinates)
        pg.display.flip()

    def update(self, screen: pg.display, args: None = None) -> None:
        """

        Update the button item on the screen (pressed <=> pressed)

        :param screen: the pygame.display element for the game
        """
        self.is_pressed = not self.is_pressed

        screen.blit(self.pressed_img if self.is_pressed else self.button_img, self.coordinates)
        pg.display.flip()
