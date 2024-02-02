"""

Screen is parameters and functions linked to screen and display

"""

import pygame as pg


class Screen:
    """

    Screen

    self.current_w : window width
    self.current_h : window height
    self.screen : pygame.screen element
    self.home_background : background for homepage
    self.main_background : background for main page
    self.menu_background : background for menu page
    self.current_background (str) : needed to select the right background to display

    """

    def __init__(self) -> None:
        self.current_w = 480
        self.current_h = 270
        self.screen = None
        self.home_background = None
        self.main_background = None
        self.menu_background = None
        self.current_background = None

        self.create_window()

    def create_window(self) -> None:
        """

        init window and game screen

        """
        pg.init()
        pg.display.set_caption("Nico the tiny myconide")
        pg.display.set_icon(pg.image.load("assets/nico_icon.png"))

        self.screen = pg.display.set_mode((self.current_w, self.current_h))
        self.home_background = pg.image.load("assets/home_background.png")
        self.main_background = pg.image.load("assets/main_background.png")
        self.menu_background = pg.image.load("assets/menu_background.png")

    def display_background(self, name: str) -> None:
        """

        Kinda explicit ngl
        :param name: name of current_screen

        """
        if name == "home":
            self.screen.blit(self.home_background, (0, 0))
            self.current_background = self.home_background
        elif name == "main":
            self.screen.blit(self.main_background, (0, 0))
            self.current_background = self.main_background
        elif name == "menu":
            self.screen.blit(self.menu_background, (0, 0))
            self.current_background = self.menu_background

    def display_screen(self, items: list) -> None:
        """

        Display items on screen like buttons or things like that

        :param items: list of buttons or things like... whatever
        """
        for item in items:
            for element in item:
                item[element].display(self.screen)

    def update_item(self, item, *args) -> None:
        """

        Sometimes, items want to be updated (like buttons being pressed)...

        :param item: the item of Item type
        :param args: additional arguments for special items (bars...)
        """
        self.screen.blit(self.current_background, item.coordinates, (item.coordinates, item.size))

        if not args:
            item.update(self.screen)
        else:
            item.update(self.screen, args)

    def display_anim(self, coordinates: list, size: list, state: int, img: str) -> None:
        """

        Display animations and effects on screen (hearts, Zzz)

        :param coordinates: coordinates of the effect
        :param size: size of effect texture
        :param state: if the effect is dynamic,
        it will have more than one state (hearts0.png, hearts1.png...)
        :param img: image of the effect
        """
        self.screen.blit(self.current_background, coordinates, (coordinates, size))

        if state:
            anim_img = pg.image.load("assets/" + img + str(state) + ".png").convert_alpha()
            self.screen.blit(anim_img, coordinates)

        pg.display.update()

    def remove_element_from_screen(self, coordinates: list, size: list) -> None:
        """
        Replace an element on the screen with background

        :param coordinates: coordinates of element
        :param size: size of element
        """
        self.screen.blit(self.current_background, coordinates, (coordinates, size))
