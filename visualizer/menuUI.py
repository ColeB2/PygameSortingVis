import pygame
from buttons import Button
from pyVariables import *
from math import ceil


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
            line_rect = [line * line_width, 25,
                        line_width-1, self.line_array[line]]
            pygame.draw.rect(self.surface, color, line_rect)
