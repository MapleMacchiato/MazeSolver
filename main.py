from graphics import Window, Line, Point
from cell import Cell
from maze import Maze


def main():

    height = 600
    width = 800
    margin = 50
    cell_width = 50
    num_rows = (height - 2 * margin) // cell_width
    num_cols = (width - 2 * margin) // cell_width
    win = Window(width, height)
    maze = Maze(margin, num_rows, num_cols, win, cell_width)
    maze.create_cells()
    maze.draw_cells()
    win.wait_for_close()


main()
