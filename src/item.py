
class Item:
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
