import os, sys
sys.path.append(os.path.join('.', 'visualizer'))
sys.path.append(os.path.join('.', 'algorithms'))
print(sys.path)
from visualizer import SortingVisualizer

if __name__ == '__main__':
    v = SortingVisualizer()
    v.main_loop()
