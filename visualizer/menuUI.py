import pygame
from buttons import Button
from pyVariables import *



class MenuUI:
    """Handles the drawing aspect of ui elements"""
    def __init__(self, screen):
        self.screen = screen


    def create_start_button(self, func):
        self.start_button = Button(x=STARTBTN_X, y=BTN_Y, width=100, height=50,
            font_size=25, color=STARTBTNCOL1, color2=STARTBTNCOL2, text='Start',
            display=self.screen, function=func)
        self.start_button.create_button()

    def create_pause_button(self, func):
        self.pause_button = Button(x=PAUSEBTN_X, y=BTN_Y, width=100, height=50,
            font_size=25, color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text='Pause',
            display=self.screen, function=func)
        self.pause_button.create_button()

    def create_next_button(self, func):
        self.next_button = Button(x=NEXTBTN_X, y=BTN_Y, width=100, height=50,
            font_size=25, color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text='>',
            display=self.screen, function=func)
        self.next_button.create_button()


class LineHandler:
    def __init__(self, screen, num_lines, line_array):
        self.screen = screen
        self.num_lines = num_lines
        self.line_array = line_array
