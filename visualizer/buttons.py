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
        font_color: Tuple formatted -> font_color=(XXX,YYY,ZZZ) - RGB values for
            color of the text, default (255,255,255) - white.
        text: Str, String value of the text to appear on the button.
        resize: Bool, Whether or not to use the built in resize function.
        display: pygame.Surface object.
        function: Function, the function the button needs to perform on click.
            Passed as so, Button(function=button_function). -> This created a
            button (using the defaults) and passes the function, button_function
            to the button to be called upon click.
    """
    def __init__(self, x=0, y=0, width=50, height=50, font_size=25,
        color=(255,51,51), color2=(0,255,128), font='arialblack',
        font_color=(255,255,255),  text='Text', resize=True, display=None,
        function=None):

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.font_size = font_size
        self.color = color
        self.color2 = color2
        self.font = font
        self.font_color = font_color
        self.text = text
        self.resize = resize
        self.display = display
        self.function = function


        self._resize_text()
        self.create_pygame_objects()
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.clicked = False




    def create_pygame_objects(self):
        """Internal method used to create pygame objects, and run pygame methods
        to handle the inital creation of the button rectangle, and font
        rectangle/text."""
        self.button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.pygame_font = pygame.font.SysFont(self.font, int(self.font_size))
        self.pygame_text = self.pygame_font.render(self.text, True, self.font_color)
        self.text_rect = self.pygame_text.get_rect()
        self.text_rect.center = (self.x + self.width/2,self.y + self.height/2)


    def _resize_text(self):
        """For internal use. Handles the sizing of the font so that the text
         can fit inside of the button."""
        if self.resize:
            if len(self.text) >= 11:
                self.font_size = self.height/4
            elif len(self.text) >=9:
                self.font_size = self.height/3
            elif len(self.text) >= 6:
                self.font_size = self.height/2 - (self.height*0.1)


    def _handle_button_click(self, *args):
        """For internal use. Handles how the button reacts, ie calls function,
        on a mouse click event, if the function exists.
        params:
            *args
        """
        if self.click[0] == 1 and self.function != None:
            self.click = True
            self.function(*args)
        else:
            None


    def _handle_button_logic(self, *args):
        """For internal use. Handles all the logic of the button. Does so by
        checking for collision, and depending on collision, drawing the button,
        and checking for clicks."""
        if self.button_rect.collidepoint((self.mouse[0]), self.mouse[1]):
            pygame.draw.rect(self.display, self.color2,
                             (self.x, self.y, self.width, self.height))
            self.display.blit(self.pygame_text, self.text_rect)
            self._handle_button_click(*args)
        else:
            pygame.draw.rect(self.display, self.color,
                             (self.x, self.y, self.width, self.height))
            self.display.blit(self.pygame_text, self.text_rect)


    def create_button(self, *args):
        """Main Button creation method
        Parameters:
            *args: *args other arguments that may need to be passed on to the
        function method which will be called by the button class.
        """
        self._handle_button_logic(*args)


if __name__ == '__main__':
    pygame.init()
    FPS=20
    fps_clock = pygame.time.Clock()

    screen = pygame.display.set_mode((600,600))
    screen.fill((255,255,255))
    pygame.display.set_caption('Button Test')

    def func():
        print('Hello World')
    b = Button(x=250, y=275, width=100,height=50, text='HW',display=screen,function=func)
    b.create_button()

    def draw():
        screen.fill((255,255,255))
        b.create_button()
        pygame.display.update()
        fps_clock.tick(30)

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
                run = False

            draw()
