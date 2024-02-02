"""

Food class used to manage food for Nico

"""

import pygame as pg
from src.item import Item


class Food(Item):
    """

    Food is a class used for food elements... yeah that's it

    :param coordinates: location on the screen of the food item
    :param size: the size of food item (normally 128x128 as cardbox texture is this size
    :param name: food name used for image and as a mini-description
    :param food_regen: how much does the food gives energy to our favourite little mushroom
    :param state: Each food element has 3 states : 2 : In Cardbox / 1 : Opened / 0 : Eaten
    """

    def __init__(
        self, coordinates: list, size: list, name: str, food_regen: float = 5, state: int = 2
    ) -> None:
        super().__init__(coordinates, size)

        self.name = name
        # Each food element has 3 states : 2 : In Cardbox / 1 : Opened / 0 : Eaten
        self.state = state
        # How much food it gives to Nico
        self.food_regen = food_regen

        # Images for state 2 and 1
        self.closed_img = pg.image.load("assets/cardbox.png").convert_alpha()
        self.opened_img = pg.image.load("assets/" + name + ".png").convert_alpha()

    def display(self, screen: pg.display) -> None:
        """

        Display Food on screen according to its state

        :param screen: the pygame.screen element for the game
        """
        if self.state == 2:
            screen.blit(self.closed_img, self.coordinates)
            pg.display.flip()
        elif self.state == 1:
            screen.blit(self.opened_img, (self.coordinates[0] + 16, self.coordinates[1] + 16))
            pg.display.flip()

    def update(self, screen, args: tuple = None) -> None:
        """

        Update the food item on the screen

        :param screen: the pygame.screen element for the game
        :param args: Can be used in the future... like if the food got rotten over time
        """
        if self.state == 2:
            self.state -= 1
            self.display(screen)
        elif self.state == 1:
            self.state -= 1
