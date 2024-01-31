import pygame as pg
from src.button import Button
from src.screen import Screen
from src.bars import Bar
from src.nico import Nico
from src.food import Food
from math import sqrt


class Game:
    def __init__(self):
        """

        Game function manage all events and element on the screen. It also updates Nico state

        """
        self.game_screen = None
        self.current_screen = 'home_screen'
        self.window = Screen()
        self.nico = None
        self.is_game_running = False
        self.current_action = {'type': 'normal', 'state': 0}
        self.old_mouse_pos = [0,0]
        self.petted_count = 0
        self.sleeping_stage = 0

        self.clock = pg.time.Clock()
        self.fps = 60
        self.time_elapsed = 0

        self.buttons = {
            'home_screen': {
                'start_button': Button([86, 170], [96, 48], 'start_button'),
                'load_button': Button([183, 170], [96, 48], 'load_button'),
                'quit_button': Button([280, 170], [96, 48], 'quit_button'),
            },
            'main_screen': {
                'menu_button': Button([447, 1], [32, 32], 'menu_button'),
                'pause_button': Button([414, 1], [32, 32], 'pause_button'),
            },
            'menu_screen': {
                'feed_button': Button([148, 87], [96, 48], 'feed_button'),
                'sleep_button': Button([245, 87], [96, 48], 'sleep_button'),
                'hygiene_button': Button([148, 136], [96, 48], 'hygiene_button'),
                'social_button': Button([245, 136], [96, 48], 'social_button'),
                'home_button': Button([447, 237], [32, 32], 'home_button'),
                'close_button': Button([447, 1], [96, 48], 'menu_button'),
            }
        }

        self.bars = {
            'energy_bar': Bar([1, 1], [120, 32], 'energy_bar', 3),
            'hunger_bar': Bar([122, 1], [120, 32], 'hunger_bar', 3),
            'hygiene_bar': Bar([1, 32], [120, 32], 'hygiene_bar', 3),
            'social_bar': Bar([122, 32], [120, 32], 'social_bar', 3),
        }

        self.dynamic = {}

    def update_screen(self):
        """

        Update the displayed screen with specific elements

        """
        self.window.screen.fill("#181425FF")

        if self.current_screen == 'home_screen':
            self.window.display_background('home')
            self.window.display_screen([
                self.buttons[self.current_screen]
            ])

        elif self.current_screen == 'main_screen':
            self.window.display_background('main')
            self.window.display_screen([
                self.buttons[self.current_screen],
                self.bars,
                self.dynamic
            ])

        elif self.current_screen == 'menu_screen':
            self.window.display_background('menu')
            self.window.display_screen([
                self.buttons[self.current_screen
            ]])

        pg.display.update()

    def is_button_pressed(self, current_btn):
        """

        Check if a button is pressed and update its animation state
        :param current_btn: the buttons on the screen
        """
        m_pos = pg.mouse.get_pos()

        for button in current_btn:
            if current_btn[button].coordinates[0] < m_pos[0] < current_btn[button].coordinates[0] + current_btn[button].size[0]:
                if current_btn[button].coordinates[1] < m_pos[1] < current_btn[button].coordinates[1] + current_btn[button].size[1]:
                    self.window.update_item(current_btn[button])
                    return button

        return None

    def is_element_clicked(self, elements, *args):
        """

        Check if an element like food or anything else other than a button is clicked and update its displayed state
        :param elements: the elements on the screen
        :param args: if an element required special variable
        """
        m_pos = pg.mouse.get_pos()
        for name in elements:
            if elements[name].coordinates[0] < m_pos[0] < elements[name].coordinates[0] + elements[name].size[0]:
                if elements[name].coordinates[1] < m_pos[1] < elements[name].coordinates[1] + elements[name].size[1]:
                    if args:
                        self.window.update_item(elements[name], args)
                    else:
                        self.window.update_item(elements[name])
                    return name

        return None

    def has_button_been_pressed(self, current_btn):
        """

        check if a button has been pressed to execute action later
        :param current_btn: buttons on the screen
        :return: the pressed button
        """
        for button in current_btn:
            if current_btn[button].is_pressed:
                self.window.update_item(current_btn[button])
                return button

        return None

    def mouse_on_nico(self, m_pos):
        """

        Check if the mouse is on Nico's hitbox

        """
        if self.nico.coordinates[0] < m_pos[0] < self.nico.coordinates[0] + self.nico.size[0]:
            if self.nico.coordinates[1] < m_pos[1] < self.nico.coordinates[1] + self.nico.size[1]:
                return True

        return False

    def home_screen_events(self, ev):
        """
        Check events on the home screen (with main menu)
        :param ev: registered event
        :return: return True if the game must continue False if it must stop
        """
        if ev.type == pg.MOUSEBUTTONDOWN:
            self.is_button_pressed(self.buttons['home_screen'])

        elif ev.type == pg.MOUSEBUTTONUP:
            button = self.has_button_been_pressed(self.buttons['home_screen'])
            if button:
                if button == 'start_button':
                    self.start_game()
                elif button == 'quit_button':
                    return False

        return True

    def main_screen_events(self, ev):
        """
        Check events on the main screen (the game)
        :param ev: registered event
        :return: only return True to continue the game
        """

        if self.current_action['type'] == 'pet':
            m_pos = pg.mouse.get_pos()

            if self.mouse_on_nico(m_pos):
                if sqrt((self.old_mouse_pos[0] - m_pos[0]) ** 2 + (self.old_mouse_pos[1] - m_pos[1]) ** 2) > 20:
                    if not self.nico.pet():
                        self.petted_count += 1

                        if not self.petted_count % 5:
                            self.current_action['state'] = self.current_action['state'] + 1 if self.current_action['state'] + 1 < 4 else 0

                        self.window.display_anim((self.nico.coordinates[0] + self.nico.size[0] + 10, self.nico.coordinates[1] - 30),(42, 74), self.current_action['state'], "hearts")
                        self.old_mouse_pos = m_pos
            else:
                self.window.display_anim((self.nico.coordinates[0] + self.nico.size[0] + 10, self.nico.coordinates[1] - 30), (42, 74),0, "hearts")

        if ev.type == pg.MOUSEBUTTONDOWN:
            pressed_button = self.is_button_pressed(self.buttons['main_screen'])

        elif ev.type == pg.MOUSEBUTTONUP:
            button = self.has_button_been_pressed(self.buttons['main_screen'])
            element_name = self.is_element_clicked(self.dynamic)

            if button:
                if button == 'menu_button':
                    self.current_screen = 'menu_screen'
                    self.update_screen()
                elif button == 'pause_button':
                    self.pause_game()
                    self.update_screen()
                    self.window.update_item(self.nico, 1)
                elif button == 'stop_button':
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)
                    self.window.remove_element_from_screen(self.buttons['main_screen']['stop_button'].coordinates, self.buttons['main_screen']['stop_button'].size)
                    del self.buttons['main_screen']['stop_button']
                    self.current_action['type'] = 'normal'
                    self.current_action['state'] = 0
                    self.petted_count = 0

            elif element_name:
                if element_name == 'food':
                    if self.dynamic['food'].state == 0:
                        if not self.nico.feed(self.dynamic['food'].food_regen):
                            del self.dynamic['food']
                        else:
                            self.dynamic['food'].state = 2
                            self.window.update_item(self.dynamic['food'])

        return True

    def menu_screen_events(self, ev):
        """
        Check events on the menu screen (select action)
        :param ev: registered event
        :return: only return True to continue the game
        """
        if ev.type == pg.MOUSEBUTTONDOWN:
            self.is_button_pressed(self.buttons['menu_screen'])

        elif ev.type == pg.MOUSEBUTTONUP:
            button = self.has_button_been_pressed(self.buttons['menu_screen'])
            if button:
                if button == 'home_button':
                    self.pause_game()
                    self.current_screen = 'home_screen'
                    self.update_screen()
                elif button == 'close_button':
                    self.current_screen = 'main_screen'
                    self.update_screen()
                elif button == 'feed_button':
                    # Create the food element to give to Nico
                    self.dynamic['food'] = Food([80, 120], [96, 96], "baby_bottle", 2.5, 2)
                    self.current_screen = 'main_screen'
                    self.update_screen()
                elif button == 'sleep_button':
                    self.current_screen = 'main_screen'
                    self.nico.isAsleep = True
                    self.update_screen()
                elif button == 'hygiene_button':
                    self.current_screen = 'main_screen'
                    self.nico.hygiene = 3
                    self.update_screen()
                elif button == 'social_button':
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                    self.buttons['main_screen']['stop_button'] = Button([447, 237], [32, 32], 'stop_button')
                    self.current_action['type'] = 'pet'
                    self.current_screen = 'main_screen'
                    self.update_screen()

        return True

    def start_game(self):
        """

        Initialized game variables and Nico states

        """

        # Create nico for the game
        self.nico = Nico(3, 3, 3, 3, False, 'happy', [180, 120], [128, 128])
        self.is_game_running = True

        self.current_screen = 'main_screen'
        self.update_screen()

    def pause_game(self):
        """

        Pause changes in game state

        """
        self.is_game_running = not self.is_game_running

    def running_game(self):
        """

        Modify variables for Nico and displays with a clock ticks. Also change Nico's animation frame

        """
        dt = self.clock.tick(self.fps)
        self.time_elapsed += dt

        # animations
        if self.current_screen == 'main_screen':
            if self.time_elapsed >= 500:
                self.window.update_item(self.nico, 1)
            else:
                self.window.update_item(self.nico, 0)

            if self.nico.isAsleep:
                if self.time_elapsed >= 750:
                    self.sleeping_stage = 3
                elif self.time_elapsed >= 500:
                    self.sleeping_stage = 2
                elif self.time_elapsed >= 250:
                    self.sleeping_stage = 1
                else:
                    self.sleeping_stage = 0

                self.window.display_anim((self.nico.coordinates[0] + self.nico.size[0] + 10, self.nico.coordinates[1] - 30), (42, 80), self.sleeping_stage, "zzz")
        if self.time_elapsed >= 1000:
            self.nico.live()
            self.nico.emotion = self.nico.feelEmotion()
            if self.current_screen == 'main_screen':
                if self.nico.isAsleep and self.bars["energy_bar"].special_state == 0:
                    self.bars["energy_bar"].update_state(1)
                elif not self.nico.isAsleep and self.bars["energy_bar"].special_state == 1:
                    self.bars["energy_bar"].update_state(0)
                    self.window.display_anim(
                        (self.nico.coordinates[0] + self.nico.size[0] + 10, self.nico.coordinates[1] - 30), (42, 80), 0, "zzz")

                self.window.update_item(self.bars["energy_bar"], self.nico.energy, -1)
                self.window.update_item(self.bars["hunger_bar"], self.nico.hunger, -1)
                self.window.update_item(self.bars["hygiene_bar"], self.nico.hygiene, -1)
                self.window.update_item(self.bars["social_bar"], self.nico.social, -1)
            self.time_elapsed = 0

    def check_event(self):
        """

        Main function to check events on screen.

        """
        value = True
        if self.is_game_running:
            self.running_game()

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                value = False
            else:
                if self.current_screen == 'home_screen':
                    value = self.home_screen_events(ev)
                else:
                    if self.current_screen == 'main_screen':
                        self.main_screen_events(ev)

                    elif self.current_screen == 'menu_screen':
                        self.menu_screen_events(ev)

                    value = True

        return value
