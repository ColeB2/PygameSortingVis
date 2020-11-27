import pygame
from random import randint
from math import ceil
from pyVariables import *
from buttons import Button
from menuUI import MenuUI, LineUI
import copy

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
        self.line_array_c = []
        self.generate_list()
        self.current_algorithm = 'Bubble'
        self.run = True
        self.run_algo = False
        self.generator = None
        self.gen_last = None
        self.MenuUI = MenuUI(screen=screen)
        self.LineUI = LineUI(screen=screen, num_lines=self.num_lines, line_array=self.line_array)
        self.array_change = False



    def main_loop(self):
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                if self.array_change:
                    self.array_change = False
                    self.draw(line_info=(None,None,None,None))
                if self.run_algo == True:
                    self.sort_handler(algo=self.get_sorting_algorithm())
                if self.gen_last:
                    self.draw(self.gen_last)
                else:
                    self.draw(line_info=(None,None,None,None))

    def get_sorting_algorithm(self):
        if self.current_algorithm == 'Bubble':
            return bubble_sort
        elif self.current_algorithm == 'Fast Bubble':
            return fast_bubble_sort
        elif self.current_algorithm == 'Selection':
            return selection_sort
        elif self.current_algorithm == 'Insertion':
            return insertion_sort
        elif self.current_algorithm == 'Shell':
            return shell_sort


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
            self.line_array_c = []

        for i in range(self.num_lines):
            line = randint(1, 200)
            self.line_array.append(line)
        self.line_array_c = copy.copy(self.line_array)


    """UI Button Functions"""
    def pause_button_function(self):
        if self.run_algo == True:
            self.run_algo = False


    def start_button_function(self):
        if self.run_algo == False:
            self.run_algo = True

    def next_button_function(self):
        """CREATE ALGORITHM GENERATOR FUNCTION"""
        if self.generator == None:
            self.generator = self.current_algorithm(self.line_array)
        line_info = next(self.generator)
        self.gen_last = (line_info)

    def _reset(self):
        self.run_algo = False
        self.array_change = True
        self.generator = None
        self.gen_last = None

    def reset_button_function(self):
        self._reset()
        self.line_array = copy.copy(self.line_array_c)
        self.LineUI.line_array = self.line_array

    def new_array_function(self):
        self._reset()
        self.generate_list()
        self.LineUI.line_array = self.line_array

    def bubble_sort_button_function(self):
        self.current_algorithm = 'Bubble'
    def fast_bubble_sort_button_function(self):
        self.current_algorithm = 'Fast Bubble'
    def selection_sort_button_function(self):
        self.current_algorithm = 'Selection'
    def insertion_sort_button_function(self):
        self.current_algorithm = 'Insertion'
    def shell_sort_button_function(self):
        self.current_algorithm = 'Shell'


    def draw_menu(self):
        self.MenuUI.create_start_button(self.start_button_function)
        self.MenuUI.create_pause_button(self.pause_button_function)
        self.MenuUI.create_next_button(self.next_button_function)
        self.MenuUI.create_reset_button(self.reset_button_function)
        self.MenuUI.create_new_array_button(self.new_array_function)
        self.MenuUI.create_bubble_sort_button(self.bubble_sort_button_function)
        self.MenuUI.create_fast_bubble_sort_button(self.fast_bubble_sort_button_function)
        self.MenuUI.create_selection_sort_button(self.selection_sort_button_function)
        self.MenuUI.create_insertion_sort_button(self.insertion_sort_button_function)
        self.MenuUI.create_shell_sort_button(self.shell_sort_button_function)



    def draw(self, line_info):
        """Handles the drawing to the screen, only method that contains the
        pygame.display.update() method to avoid update multiple times in
        multiple places."""
        screen.fill(WHITE2)
        self.LineUI.draw_lines(line_info)
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
            pygame.time.wait(10)


if __name__ == '__main__':
    S = SortingVisualizer()
    S.main_loop()
