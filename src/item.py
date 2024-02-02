"""

Abstract class for item of the game (bars, buttons, food...)

"""


class Item:
    """

    Item

    coordinates : coordinates of item on the screen
    size : size of item texture/hitbox

    """

    def __init__(self, coordinates: list, size: list) -> None:
        self.coordinates = coordinates
        self.size = size

    def display(self, screen) -> None:
        """

        Display Item on screen

        """
        raise NotImplementedError

    def update(self, screen, args: tuple) -> None:
        """

        Update Item on screen

        """
        raise NotImplementedError
