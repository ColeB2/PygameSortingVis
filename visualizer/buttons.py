'''
buttons.py - Button class that has numberous variables to make buttons easier
'''
from pyVariables import * #To handle colors
import pygame
from pygame.locals import *

class Button:
    """
    A class to aid in the creation of buttons in Pygame. Currently packaged
    with pyVariables to handle basic colors, can be replaced

    Attributes:
        x: Int, x value for the top left corner of the button, default 0.
        y: Int, y value for the top left corner of the button, default 0
        width: Int, width(x dimension) of the button in pixels, default 50.
        height: Int, height(y dimension) of the button in pixels, default 50.
        font_size: Int, size of the font on the button, default 25.
        color: Tuple formated -> color=(XXX,YYY,ZZZ) - RGB values for color of
            button initial state, default (0,255,128) - green.
        color2: Tuple formatted -> color2=(XXX,YYY,ZZZ) - RGB values for color
            of button while button is hovered over, default (255,51,51) - red.
        font: Str, font type for the text, default 'arialblack'
        text: Str, String value of the text to appear on the button.
        text_color: Tuple formatted -> text_color=(XXX,YYY,ZZZ) - RGB values for
            color of the text, default (0,0,0) - black.
        display: pygame.Surface object.
        function: Function, the function the button needs to perform on click.
            Passed as so, Button(function=button_function). -> This created a
            button (using the defaults) and passes the function, button_function
            to the button to be called upon click.



    """
    def __init__(self, x=0, y=0, width=50, height=50, font_size=25,
        color=(255,51,51), color2=(0,255,128), font='arialblack', text='Text',
        text_color=(0,0,0), display=None, function=None):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.color = color
        self.color2 = color2
        self.font = font
        self.text = text
        self.text_color = text_color
        self.display = display
        self.function = function

        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.clicked = False

    def text_length(self):
        if len(self.text) >= 12:
            self.font_size = self.height/4
        elif len(self.text) >=9:
            self.font_size = self.height/3
        elif len(self.text) >= 6:
            self.font_size = self.height/2 - (self.height*0.1)

    def handle_button_colors(self):
        # if (self.x + self.width > self.mouse[0] > self.x and
        #     self.y + self.height > self.mouse[1] > self.y):

        if self.button_rect.collidepoint((self.mouse[0], self.mouse[1])):
            pygame.draw.rect(self.display, self.color2,
                            (self.x, self.y, self.width, self.height))

            self.handle_button_click()

        else:
            pygame.draw.rect(self.display, self.color,
                            (self.x, self.y, self.width, self.height))


    def handle_button_click(self):
        if self.click[0] == 1 and self.function != None:
            if self.click[0] == 0:
                print(self.click)
            self.click = True
            self.function()
        else:
            None


    def create_button(self):
        '''Displays the button with text, and multiple colours on the screen'''
        self.text_length()
        self.handle_button_colors()

        font = pygame.font.SysFont(self.font, int(self.font_size))
        text = font.render(self.text, True, WHITE)
        text_rect = text.get_rect()
        text_rect.center = (self.x + self.width/2,
                            self.y + self.height/2)
        self.display.blit(text, text_rect)
