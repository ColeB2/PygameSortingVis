import pygame
from random import randint
from math import ceil
from pyVariables import *
from buttons import Button

"""Import set up to be able to run from visalizer.py/main.py for dev purposes"""
if __name__ == '__main__':
    import os, sys
    sys.path.append(os.path.join('.', 'algorithms'))
    from algorithms import (
        bubble_sort, fast_bubble_sort, selection_sort, insertion_sort,
        shell_sort
        )
else:
    from algorithms.algorithms import (
        bubble_sort, fast_bubble_sort, selection_sort, insertion_sort,
        shell_sort
        )
"""
TODO LIST:
- Create algorithm generator FUNCTION
- Further refactoring
- Break up code, UI things and functional things
- Add more algorithms
- Algorithm select buttons
- Speed select buttons, slider?
- Reset Button
- New Array button
- Rewind button?
"""
"""Pygame code to set up screen"""
pygame.init()
screen = pygame.display.set_mode(DIS_SIZE)
screen.fill(WHITE2)
pygame.display.set_caption('Sorting Visualizer')


class SortingVisualizer:

    def __init__(self):
        self.num_lines = 50
        self.speed = 0
        self.line_array = []
        self.generate_list()
        self.current_algorithm = insertion_sort
        self.run = True
        self.run_algo = False
        self.generator = None
        self.gen_last = None



    def main_loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False


                if self.run_algo == True:
                    self.sort_handler(algo=self.current_algorithm)
                if self.gen_last:
                    self.draw(self.gen_last)
                else:
                    self.draw(line_info=(None,None,None,None))


    def sort_handler(self, algo):
        """Handles the sorting algorithms. Does so by creating a generator using
        the given algorithm, and then handling how the generator runs to produce
        output on the screen. Contains a pause feature, but adding last value
        to a variable when the generator main loop breaks."""
        if self.generator == None:
            self.generator = algo(self.line_array)
        while self.run_algo:
            for line_info in self.generator:
                if self.run_algo:
                    self.update_lines(line_info)
                else:
                    self.gen_last = line_info
                    break





    def generate_list(self):
        if self.num_lines != 0:
            self.line_array = []

        for i in range(self.num_lines):
            line = randint(1, 200)
            self.line_array.append(line)

    def pause_button(self):
        if self.run_algo == True:
            self.run_algo = False


    def start_button(self):
        if self.run_algo == False:
            self.run_algo = True

    def next_button(self):
        """CREATE ALGORITHM GENERATOR FUNCTION"""
        if self.generator == None:
            self.generator = self.current_algorithm(self.line_array)
        line_info = next(self.generator)
        self.gen_last = (line_info)


    def draw_menu(self):
        self.StartButton = Button(x=STARTBTN_X, y=BTN_Y, width=100, height=50,
            font_size=25, color=STARTBTNCOL1, color2=STARTBTNCOL2, text='Start',
            display=screen, function=self.start_button)
        self.StartButton.create_button()

        self.PauseButton = Button(x=PAUSEBTN_X, y=BTN_Y, width=100, height=50,
            font_size=25, color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text='Pause',
            display=screen, function=self.pause_button)
        self.PauseButton.create_button()

        self.NextButton = Button(x=NEXTBTN_X, y=BTN_Y, width=100, height=50,
            font_size=25, color=PAUSEBTNCOL1, color2=PAUSEBTNCOL2, text='>',
            display=screen, function=self.next_button)
        self.NextButton.create_button()



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
            pygame.draw.rect(screen, color, line_rect)



    def draw(self, line_info):
        """Handles the drawing to the screen, only method that contains the
        pygame.display.update() method to avoid update multiple times in
        multiple places."""
        screen.fill(WHITE2)
        self.draw_lines(line_info)
        self.draw_menu()
        pygame.display.update()

    def update_lines(self, line_info):
        """Updates the lines in the program.  Does so by calling the draw
        function when the algorithms are running."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if self.run_algo:
            self.draw(line_info)
            pygame.time.wait(100)


if __name__ == '__main__':
    S = SortingVisualizer()
    S.main_loop()
