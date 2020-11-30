import pygame
from buttons import Button
from pyVariables import *
from math import ceil



class MenuUI:
    """Handles the drawing aspect of ui elements"""
    def __init__(self, screen):
        self.screen = screen


    def create_start_button(self, func):
        self.start_button = Button(x=STARTBTN_X, y=BTN_Y2, width=100, height=50,
            font_size=25, color=STARTBTNCOL1, color2=STARTBTNCOL2, text='Start',
            display=self.screen, function=func)
        self.start_button.create_button()


    def create_pause_button(self, func):
        self.pause_button = Button(x=PAUSEBTN_X, y=BTN_Y2, width=100, height=50,
            font_size=25, color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text='Pause',
            display=self.screen, function=func)
        self.pause_button.create_button()


    def create_next_button(self, func):
        self.next_button = Button(x=NEXTBTN_X, y=BTN_Y2, width=100, height=50,
            font_size=25, color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text='>',
            display=self.screen, function=func)
        self.next_button.create_button()


    def create_reset_button(self, func):
        self.reset_button = Button(x=NEXTBTN_X+125, y=BTN_Y2, width=100, height=50,
            font_size=25, color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text='Reset',
            display=self.screen, function=func)
        self.reset_button.create_button()


    def create_new_array_button(self,func):
        self.new_array_button = Button(x=NEXTBTN_X+250, y=BTN_Y2, width=100, height=50,
            font_size=25, color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text='New Array',
            display=self.screen, function=func)
        self.new_array_button.create_button()


    def create_algo_buttons(self, func):
        algos = ['Bubble', 'Fast Bubble', 'Selection', 'Insertion', 'Shell']
        for i in range(len(algos)):
            new_button = Button(
                x=(50+(i*125)), y = BTN_Y, width=100, height=50, font_size=25,
                color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text=algos[i],
                display=self.screen, function=func)
            new_button.create_button(new_button.text)


class LineUI:
    """Handles the drawing of the lines"""
    def __init__(self, screen, num_lines, line_array):
        self.screen = screen
        self.num_lines = num_lines
        self.line_array = line_array


    def draw_lines(self, line_info):
        """
        Draws the all the lines, as well as colors the lines given their own
        special colors

        line1, line2 - Highlight lines - colored w LINE_HIGHLIGHT color.
        line3, line4 - Swapping lines - colored w LINE_SWAP color.
        """
        for line in range(self.num_lines):
            color = LINE_COLOR

            if len(line_info) == 5:
                if line_info[4][0] == 'insert':
                    if line == line_info[4][1]:
                        color = INSERTION_LINE
                    elif line <= line_info[4][1]:
                        color = LINE_COLOR
                    else:
                        color = FADED_BLUE
                if line_info[4][0] == 'bubble':
                    if line >= line_info[4][1]:
                        color = SUB_ARRAY_COLOR

                if line_info[4][0] == 'shell':
                    gap = line_info[4][1]
                    i = line_info[4][2]
                    try:
                        j = line_info[4][3]
                    except:
                        j = None
                    if line == j:
                        color = INSERTION_LINE
                    elif line == i:
                        color = LINE_COLOR
                    elif line % gap == i % gap:
                        color = LINE_COLOR

                    else:
                        color = FADED_BLUE



            if line == line_info[0]  or line == line_info[1]:
                color = LINE_HIGHLIGHT
            if line == line_info[2] or line == line_info[3]:
                color = LINE_SWAP

            line_width = ceil(DIS_X/self.num_lines)
            line_rect = [line * line_width, 0,
                        line_width-1, self.line_array[line]]
            pygame.draw.rect(self.screen, color, line_rect)
