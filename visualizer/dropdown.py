"""
dropdown.py - DropDown menu created using pygame.
"""
import pygame
from pygame.locals import *

from buttons import Button


class DropDown:
    """
    """
    def __init__(self, x=0, y=0, width=50, height=20, font_size=25,
        color=(255,51,51), color2=(0,255,128), font='arialblack',
        font_color=(255,255,255), text='Text', resize=False, display=None):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.color = color
        self.color2 = color2
        self.font = font
        self.font_color = font_color
        self.text = self.text
        self.resize = resize
        self.display = display
        self.function = function

        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.clicked = False

        self.num_menu_option = 0


    def _drop_down_menu(self, func):
        for i in range(len(self.drop_down_list)):
            new_option = Button(
                x=self.x, y=(self.y + (i*height)), width=self.width,
                height=self.height, font_size=self.font_size, color=self.color,
                color2=self.color2, text=self.text, display=self.display,
                function=func

            )





    def create_menu(self):
        self.drop_down_button = Button(x=self.x, y=self.y,width=self.width,
            height=self.height, font_size=self.font_size, color=self.color,
            font=self.font, font_color=self.font_color, text=self.text,
            resize=self.resize, display=self.display, function=None)


    def new_menu_item(self, func):
        self.num_menu_option += 1
        new_option = Button(
            x=self.x, y=self.y+(self.num_menu_option*height), width=self.width,
            height=self.height, font_size=self.font_size, color=self.color,
            color2=self.color2, text=self.text, display=self.display,
            function=func
        )
        new_option.create_button()


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((600,600))
    screen.fill((255,255,255))
    pygame.display.set_caption('Button Test')
    def func(string):
        return string
    b = Button(x=250, y=275, width=100,height=50, display=screen,function=func)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                run = False

            screen.fill((255,255,255))
            b.create_button('string')
            pygame.display.update()
