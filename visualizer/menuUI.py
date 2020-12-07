import pygame
from buttons import Button
from pyVariables import *
from math import ceil



class MenuUI:
    """Handles the drawing aspect of ui elements"""
    def __init__(self, surface):
        self.surface = surface


    def create_start_button(self, func):
        self.start_button = Button(rect=(STARTBTN_X, BTN_Y2, 100, 50),
            font_size=25, color=STARTBTNCOL1, color2=STARTBTNCOL2, text='Start',
            function=func)
        #self.start_button.create_button()


    def create_pause_button(self, func):
        self.pause_button = Button(rect=(PAUSEBTN_X, BTN_Y2, 100, 50),
            font_size=25, color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text='Pause',
            function=func)


    def create_next_button(self, func):
        self.next_button = Button(rect=(NEXTBTN_X, BTN_Y2, 100, 50),
            font_size=25, color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text='>',
            display=self.surface, function=func)
        self.next_button.create_button()


    def create_reset_button(self, func):
        self.reset_button = Button(rect=(NEXTBTN_X+125, BTN_Y2, 100, 50),
            font_size=25, color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text='Reset',
            display=self.surface, function=func)
        self.reset_button.create_button()


    def create_new_array_button(self,func):
        self.new_array_button = Button(rect=(NEXTBTN_X+250, BTN_Y2, 100, 50),
            font_size=25, color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text='New Array',
            display=self.surface, function=func)
        self.new_array_button.create_button()


    def create_algo_buttons(self, func, *args):
        algos = ['Bubble', 'Fast Bubble', 'Selection', 'Insertion', 'Shell',
            'Merge', 'Quick Sort', 'Heap']
        for i in range(len(algos)):
            new_button = Button(
                rect=( (50+(i*125)), BTN_Y, 100, 50), font_size=25,
                color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text=algos[i],
                display=self.surface, function=func)
            new_button.create_button(new_button.text)


class LineUI:
    """Handles the drawing of the lines"""
    def __init__(self, surface, num_lines, line_array):
        self.surface = surface
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

                if line_info[4][0] == 'quick':
                    if line == line_info[4][1]:
                        color = INSERTION_LINE


                if line_info[4][0] == 'splitting':
                    # print(line)
                    if line == line_info[4][3]:
                        color = INSERTION_LINE
                    elif line < line_info[4][3]:
                        color = SUB_ARRAY_COLOR
                    elif line > line_info[4][3]:
                        color = LIGHT_RED



            if line == line_info[0]  or line == line_info[1]:
                color = LINE_HIGHLIGHT
            if line == line_info[2] or line == line_info[3]:
                color = LINE_SWAP

            line_width = ceil(DIS_X/self.num_lines)
            line_rect = [line * line_width, 0,
                        line_width-1, self.line_array[line]]
            pygame.draw.rect(self.surface, color, line_rect)
