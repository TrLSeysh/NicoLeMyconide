import pygame as pg
from src.button import Button
from src.screen import Screen


class Game:
    def __init__(self):
        self.game_screen = None
        self.current_screen = 'home_screen'
        self.window = Screen()

        self.buttons = {
            'home_screen': {
                'start_button': Button(196, 140, 96, 48, 'main_button', self.window.screen),
                'quit_button': Button(196, 200, 96, 48, 'main_button', self.window.screen),
            },
            'main_screen': {
                'menu_button': Button(10, 10, 96, 48, 'main_button', self.window.screen),
                'pause_button': Button(10, 10, 96, 48, 'main_button', self.window.screen),
                'speed_button': Button(10, 10, 96, 48, 'main_button', self.window.screen),
            },
            'menu_screen': {
                'feed_button': Button(10, 10, 96, 48, 'main_button', self.window.screen),
                'sleep_button': Button(10, 10, 96, 48, 'main_button', self.window.screen),
                'home_button': Button(10, 10, 96, 48, 'main_button', self.window.screen),
                'close_button': Button(10, 10, 96, 48, 'main_button', self.window.screen),
            }
        }

    def update_screen(self):
        if self.current_screen == 'home_screen':
            self.window.display_screen([self.buttons[self.current_screen]])
        elif self.current_screen == 'main_screen':
            self.window.display_screen([self.buttons[self.current_screen]])
        elif self.current_screen == 'menu_screen':
            self.window.display_screen([self.buttons[self.current_screen]])

    def is_button_pressed(self, current_btn):
        m_pos = pg.mouse.get_pos()

        for button in current_btn:
            if current_btn[button].x < m_pos[0] < current_btn[button].x + current_btn[button].size_x:
                if current_btn[button].y < m_pos[1] < current_btn[button].y + current_btn[button].size_y:
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

        return True

    def menu_screen_events(self, ev):
        pass

    def start_game(self):
        self.current_screen = 'main_screen'
        self.update_screen()

    def check_event(self):
        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                return False

            if self.current_screen == 'home_screen':
                return self.home_screen_events(ev)

            if self.current_screen == 'main_screen':
                return self.main_screen_events(ev)

            if self.current_screen == 'menu_screen':
                return self.menu_screen_events(ev)

        return True
