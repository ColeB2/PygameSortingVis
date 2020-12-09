"""
dropdown.py - DropDown menu created using pygame.
"""
import pygame
from pygame.locals import *

from buttons import Button


class DropDown:
    """
    """
    def __init__(self, rect, **kwargs):
        self.rect = pygame.Rect(rect)
        self.optional_settings(kwargs)
        self.render_text()
        self.clicked = False
        self.hovered = False

        self.y = self.rect[1]
        self.h = self.rect[3]
        self.num_options = 0
        self.all_menu_items = []

        self.create_menu()

    def open_menu(self):
        print(self.all_menu_items)
        for button in self.all_menu_items:
            print(button[0])
            button[0].update(button[1])

    def create_menu(self):
        self.menu = Button(rect=self.rect, function=self.open_menu, text='DropDown')


    def render_text(self):
        """Internal method used to pre render the button text."""
        if self.text:
            self.pygame_text = self.font.render(self.text, True, self.font_color)
            self.text_rect = self.pygame_text.get_rect()
            self.text_rect.center = self.rect.center


    def optional_settings(self, kwargs):
        """Method used to change optional settings on button."""
        options = {'text': None,
                   'font': pygame.font.Font(None, 25),
                   'color': (0,255,128),
                   'hover_color': (255,51,51),
                   'font_color': (255,255,255),
                   'run_on_release': True,
                   }

        for kwarg in kwargs:
            if kwarg in options:
                options[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError(f"Button option {kwarg} does not exist")
        self.__dict__.update(options)


    def new_option(self, func, surface):
        b = Button(rect=(self.rect[0], (self.y+(self.h*(1+self.num_options))),
                         self.rect[2], self.h),
                         function=func)
        self.num_options += 1
        self.all_menu_items.append((b,surface))

    def get_event(self, event):
        for button in self.all_menu_items:
            button[0].get_event(event)

    def update(self, surface):
        self.menu.update(surface)

if __name__ == '__main__':
    pygame.init()
    surface = pygame.display.set_mode((600,600))
    surface.fill((255,255,255))
    pygame.display.set_caption('Button Example')

    def func():
        print('Hello World')

    b = Button(rect=(250,250,100,50), function=func, text='Hello World')
    dd = DropDown(rect=(0,0,200,25), text='Menu')
    dd.new_option(func=func, surface=surface)
    dd.new_option(func=func, surface=surface)




    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            b.get_event(event)
            dd.menu.get_event(event)
            dd.get_event(event)


        b.update(surface)
        dd.update(surface)
        pygame.display.update()
