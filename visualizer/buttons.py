'''
buttons.py - Button class that has numberous variables to make buttons easier
'''
import pygame
from pygame.locals import *

class Button:
    """
    A class to aid in the creation of buttons in Pygame. Currently packaged
    with pyVariables to handle basic colors, can be replaced

    Attributes:
        rect: Tuple of int values -> (top, left, width, height), default (0,0,50,50)
        font_size: Int, size of the font on the button, default 25.
        color: Tuple formated -> color=(XXX,YYY,ZZZ) - RGB values for color of
            button initial state, default (0,255,128) - green.
        color2: Tuple formatted -> color2=(XXX,YYY,ZZZ) - RGB values for color
            of button while button is hovered over, default (255,51,51) - red.
        font: Str, font type for the text, default 'arialblack'
        font_color: Tuple formatted -> font_color=(XXX,YYY,ZZZ) - RGB values for
            color of the text, default (255,255,255) - white.
        text: Str, String value of the text to appear on the button.
        resize: Bool, Whether or not to use the built in resize function.
        function: Function, the function the button needs to perform on click.
            Passed as so, Button(function=button_function). -> This created a
            button (using the defaults) and passes the function, button_function
            to the button to be called upon click.
    """
    def __init__(self, rect=(0,0,100,50), font_size=25,
        color=(255,51,51), color2=(0,255,128), font=None,
        font_color=(255,255,255),  text='Text', function=None):

        self.rect = pygame.Rect(rect)
        self.color = color
        self.color2 = color2
        self.font_size = int(font_size)
        self.font_color = font_color
        self.text = text
        self.font = pygame.font.Font(font, self.font_size)
        self.render_text()
        self.function = function
        self.click = pygame.mouse.get_pressed()
        self.clicked = False
        self.hovered = False


    def render_text(self):
        """Internal method used to pre render the button text."""
        if self.text:
            self.pygame_text = self.font.render(self.text, True, self.font_color)
            self.text_rect = self.pygame_text.get_rect()
            self.text_rect.center = self.rect.center

    def get_event(self, event, *args):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self._handle_button_click(*args)


    def _handle_button_click(self, *args):
        """For internal use. Handles how the button reacts, ie calls function,
        on a mouse click event, if the function exists.
        params:
            *args
        """
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            #self.clicked = True
            self.function(*args)

    def button_hover(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if self.hovered == False:
                self.hovered = True
        else:
            self.hovered = False

    def update(self, surface, *args):
        color = self.color
        text = self.text
        self.button_hover()
        if self.clicked and self.color2:
            color = self.color2
        elif self.hovered:
            color = self.color2

        pygame.draw.rect(surface, color, self.rect)
        surface.blit(self.pygame_text, self.text_rect)



    def _handle_button_logic(self, *args):
        """For internal use. Handles all the logic of the button. Does so by
        checking for collision, and depending on collision, drawing the button,
        and checking for clicks."""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(surface, self.color2, self.rect)
            surface.blit(self.pygame_text, self.text_rect)
            self._handle_button_click(*args)
        else:
            pygame.draw.rect(surface, self.color, self.rect)
            surface.blit(self.pygame_text, self.text_rect)


    def create_button(self, *args):
        """Main Button creation method
        Parameters:
            *args: *args other arguments that may need to be passed on to the
        function method which will be called by the button class.
        """
        self._handle_button_logic(*args)


if __name__ == '__main__':
    pass
