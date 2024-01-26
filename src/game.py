import pygame as pg
from src.button import Button
from src.screen import Screen
from src.bars import Bar


class Game:
    def __init__(self):
        self.game_screen = None
        self.current_screen = 'home_screen'
        self.window = Screen()

        self.buttons = {
            'home_screen': {
                'start_button': Button([196, 140], [96, 48], 'main_button'),
                'quit_button': Button([196, 200], [96, 48], 'main_button'),
            },
            'main_screen': {
                'menu_button': Button([447, 1], [32, 32], 'menu_button'),
                'pause_button': Button([414, 1], [32, 32], 'pause_button'),
            },
            'menu_screen': {
                'feed_button': Button([148, 87], [96, 48], 'main_button'),
                'sleep_button': Button([245, 87], [96, 48], 'main_button'),
                'hygiene_button': Button([148, 136], [96, 48], 'main_button'),
                'social_button': Button([245, 136], [96, 48], 'main_button'),
                'home_button': Button([447, 237], [32, 32], 'pause_button'),
                'close_button': Button([447, 1], [96, 48], 'menu_button'),
            }
        }

        self.bars = {
            'energy_bar': Bar([1, 1], [80, 20], 'energy_bar', 2.8),
        }

    def update_screen(self):
        if self.current_screen == 'home_screen':
            self.window.display_screen([
                self.buttons[self.current_screen]
            ])

        elif self.current_screen == 'main_screen':
            self.window.display_screen([
                self.buttons[self.current_screen],
                self.bars
            ])

        elif self.current_screen == 'menu_screen':
            self.window.display_screen([self.buttons[self.current_screen]])

    def is_button_pressed(self, current_btn):
        m_pos = pg.mouse.get_pos()

        for button in current_btn:
            if current_btn[button].coordinates[0] < m_pos[0] < current_btn[button].coordinates[0] + current_btn[button].size[0]:
                if current_btn[button].coordinates[1] < m_pos[1] < current_btn[button].coordinates[1] + current_btn[button].size[1]:
                    self.window.update_item(current_btn[button])
                    return button

        return None

    def has_button_been_pressed(self, current_btn):
        for button in current_btn:
            if current_btn[button].is_pressed:
                self.window.update_item(current_btn[button])
                return button

        return None

    def home_screen_events(self, ev):
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
        if ev.type == pg.MOUSEBUTTONDOWN:
            self.is_button_pressed(self.buttons['main_screen'])

        elif ev.type == pg.MOUSEBUTTONUP:
            button = self.has_button_been_pressed(self.buttons['main_screen'])
            if button:
                if button == 'menu_button':
                    self.current_screen = 'menu_screen'
                    self.update_screen()
                elif button == 'pause_button':
                    self.window.update_item(self.bars["energy_bar"], None, 1)
                    self.update_screen()

        return True

    def menu_screen_events(self, ev):
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

        return True

    def start_game(self):
        self.current_screen = 'main_screen'
        self.update_screen()

    def pause_game(self):
        pass

    def check_event(self):
        value = True

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
