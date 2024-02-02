"""

Abstract class for item of the game (bars, buttons, food...)

"""


class Item:
    """

    coordinates : coordinates of item on the screen
    size : size of item texture/hitbox

    """
    def __init__(self, coordinates, size):
        self.coordinates = coordinates
        self.size = size

    def display(self, screen):
        """

        Display Item on screen

        """
        raise NotImplementedError

    def update(self, screen, args):
        """

        Update Item on screen

        """
        raise NotImplementedError
