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
        shell_sort, merge_sort, heap_sort, quick_sort
        )
else:
    from algorithms.algorithms import (
        bubble_sort, fast_bubble_sort, selection_sort, insertion_sort,
        shell_sort, merge_sort, heap_sort, quick_sort
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
- shell sort will sometimes finish in a compare viewset
- next button sometimes crashes - stop iteration?
- Clicking next, then resuming play can leave lines wrong color
- Light blue blinking on Merge, Check.


"""
"""Pygame code to set up surface"""
pygame.init()
surface = pygame.display.set_mode(DIS_SIZE)
surface.fill(WHITE2)
pygame.display.set_caption('Sorting Visualizer')


class SortingVisualizer:
    def __init__(self):
        self.num_lines = 25
        self.speed = 0
        self.line_array = []
        self.line_array_c = []
        self.generate_list()
        self.current_algorithm = 'Insertion'
        self.run = True
        self.run_algo = False
        self.generator = None
        self.gen_last = None
        self.array_change = False
        self.complete = False
        self.MenuUI = MenuUI(surface=surface)
        self.LineUI = LineUI(surface=surface, num_lines=self.num_lines,
            line_array=self.line_array)



    def main_loop(self):
        """Main Program Loop pygame."""
        self.create_buttons()
        while self.run:
            """Main Loop Event Handling"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False

                self.start_button.get_event(event)
                self.pause_button.get_event(event)
                self.next_button.get_event(event)
                self.reset_button.get_event(event)
                self.new_array_button.get_event(event)

            """Main Loop Logic Handling"""
            if not self.generator:
                algo = self.get_sorting_algorithm()
                self.generator = algo(self.line_array)

            if self.run_algo:
                try:
                    line_info = next(self.generator)
                    self.gen_last = line_info
                except StopIteration:
                    line_info = (None,None,None,None)
                    self.gen_last = None

            elif not self.run_algo:
                if self.gen_last:
                    line_info = self.gen_last
                elif self.array_change:
                    self.array_change = False
                    line_info = (None,None,None,None)
                else:
                    line_info = (None,None,None,None)


            """Main Loop Drawing"""
            self.draw(line_info)
            pygame.time.wait(10)


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
        elif self.current_algorithm == 'Quick Sort':
            return quick_sort


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
            algo = self.get_sorting_algorithm()
            self.generator = algo(self.line_array)
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
        self.start_button.update(surface)
        self.pause_button.update(surface)
        self.next_button.update(surface)
        self.reset_button.update(surface)
        self.new_array_button.update(surface)


    def create_buttons(self):
        self.start_button = Button(rect=(STARTBTN_X, BTN_Y2, 100, 50),
            color=STARTBTNCOL1, hover_color=STARTBTNCOL2, text='Start',
            function=self.start_button_function)
        self.pause_button = Button(rect=(PAUSEBTN_X, BTN_Y2, 100, 50),
            color=PAUSEBTNCOL1, hover_color=PAUSEBTNCOL2, text='Pause',
            function=self.pause_button_function)
        self.next_button = Button(rect=(NEXTBTN_X, BTN_Y2, 100, 50),
            color=PAUSEBTNCOL1, hover_color=PAUSEBTNCOL2, text='>',
            function=self.next_button_function)
        self.reset_button = Button(rect=(NEXTBTN_X+125, BTN_Y2, 100, 50),
            color=PAUSEBTNCOL1, hover_color=PAUSEBTNCOL2, text='Reset',
            function=self.reset_button_function)
        self.new_array_button = Button(rect=(NEXTBTN_X+250, BTN_Y2, 100, 50),
            color=PAUSEBTNCOL1, hover_color=PAUSEBTNCOL2, text='New Array',
            function=self.new_array_function)

    def create_algo_buttons(self):
        self.bubble_sort_button = Button(rect=0,0,100,50, text='Bubble',
            function=self.bubble_sort_function)


    def draw(self, line_info):
        """Handles the drawing to the surface, only method that contains the
        pygame.display.update() method to avoid update multiple times in
        multiple places."""
        surface.fill(WHITE2)
        self.LineUI.draw_lines(line_info)
        self.draw_menu()
        pygame.display.update()



if __name__ == '__main__':
    S = SortingVisualizer()
    S.main_loop()
