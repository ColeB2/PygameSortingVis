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
        shell_sort, merge_sort, heap_sort
        )
else:
    from algorithms.algorithms import (
        bubble_sort, fast_bubble_sort, selection_sort, insertion_sort,
        shell_sort, merge_sort, heap_sort
        )
"""
TODO LIST:
- Further refactoring
- Break up code, UI things and functional things
- Add more algorithms ---- Heap, Merge(more work), Quick-Sort
- Algorithm select dropdown menu?
- Speed select buttons, slider?
- Rewind button?

Known Bugs:
-Running program again with already solved array - being able to
"""
"""Pygame code to set up screen"""
pygame.init()
screen = pygame.display.set_mode(DIS_SIZE)
screen.fill(WHITE2)
pygame.display.set_caption('Sorting Visualizer')


class SortingVisualizer:

    def __init__(self):
        self.num_lines = 25
        self.speed = 0
        self.line_array = []
        self.line_array_c = []
        self.generate_list()
        self.current_algorithm = 'Merge'
        self.run = True
        self.run_algo = False
        self.generator = None
        self.gen_last = None
        self.MenuUI = MenuUI(screen=screen)
        self.LineUI = LineUI(screen=screen, num_lines=self.num_lines, line_array=self.line_array)
        self.array_change = False
        self.complete = False



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
        elif self.current_algorithm == 'Merge':
            return merge_sort
        elif self.current_algorithm == 'Heap':
            return heap_sort


    def sort_handler(self, algo):
        """Handles the sorting algorithms. Does so by creating a generator using
        the given algorithm, and then handling how the generator runs to produce
        output on the screen. Contains a pause feature, but adding last value
        to a variable when the generator main loop breaks."""
        if self.generator == None:
            self.generator = algo(self.line_array)
        while self.run_algo:
            for line_info in self.generator:
                if line_info == 'Complete':
                    self.run_algo = False
                    self.complete = True
                    self.update_lines(line_info=(None, None,None, None))
                elif self.run_algo:
                    self.update_lines(line_info)
                else:
                    self.gen_last = line_info
                    break





    def generate_list(self):
        if self.num_lines != 0:
            self.line_array = []
            self.line_array_c = []

        for i in range(self.num_lines):
            line = randint(1, 400)
            self.line_array.append(line)
        self.line_array_c = copy.copy(self.line_array)


    """UI Button Functions"""
    def pause_button_function(self):
        if self.run_algo == True:
            self.run_algo = False


    def start_button_function(self):
        if self.run_algo == False and self.complete == False:
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
        self.complete = False

    def reset_button_function(self):
        self._reset()
        self.line_array = copy.copy(self.line_array_c)
        self.LineUI.line_array = self.line_array

    def new_array_function(self):
        self._reset()
        self.generate_list()
        self.LineUI.line_array = self.line_array


    def algo_button_function(self, button_text):
        self.current_algorithm = str(button_text)


    def draw_menu(self):
        self.MenuUI.create_start_button(self.start_button_function)
        self.MenuUI.create_pause_button(self.pause_button_function)
        self.MenuUI.create_next_button(self.next_button_function)
        self.MenuUI.create_reset_button(self.reset_button_function)
        self.MenuUI.create_new_array_button(self.new_array_function)
        self.MenuUI.create_algo_buttons(self.algo_button_function)



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
