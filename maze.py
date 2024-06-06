from cell import Cell
from graphics import Point
import time
import random


class Maze:

    def __init__(self, margin, num_rows, num_cols, canvas, cell_width):
        self.margin = margin
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.canvas = canvas
        self.cells = []
        self.cell_width = cell_width

    def create_cells(self):
        start_point = Point(self.margin + self.cell_width /
                            2, self.margin + self.cell_width/2)

        for x in range(self.num_cols):
            col_cells = []
            for y in range(self.num_rows):
                cell = Cell(
                    self.canvas,
                    Point(start_point.x + x*self.cell_width,
                          start_point.y + y*self.cell_width),
                    self.cell_width)
                cell.draw()
                self.animate()
                col_cells.append(cell)
            self.cells.append(col_cells)

    def animate(self):
        self.canvas.redraw()
        time.sleep(0.02)

    def break_entrance_and_exit(self):
        self.cells[0][0].has_top_wall = False
        self.cells[0][0].draw()
        self.cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self.cells[self.num_cols-1][self.num_rows-1].draw()

    def break_walls(self, i, j):
        self.cells[i][j].visited = True
        while True:
            next_index_list = []

            # determine which cell(s) to visit next
            # left
            if i > 0 and not self.cells[i - 1][j].visited:
                next_index_list.append((i - 1, j))
            # right
            if i < self.num_cols - 1 and not self.cells[i + 1][j].visited:
                next_index_list.append((i + 1, j))
            # up
            if j > 0 and not self.cells[i][j - 1].visited:
                next_index_list.append((i, j - 1))
            # down
            if j < self.num_rows - 1 and not self.cells[i][j + 1].visited:
                next_index_list.append((i, j + 1))

            # if there is nowhere to go from here
            # just break out
            if len(next_index_list) == 0:
                self.cells[i][j].draw()
                self.animate()
                return

            # randomly choose the next direction to go
            direction_index = random.randrange(len(next_index_list))
            next_index = next_index_list[direction_index]

            # knock out walls between this cell and the next cell(s)
            # right
            if next_index[0] == i + 1:
                self.cells[i][j].has_right_wall = False
                self.cells[i + 1][j].has_left_wall = False
            # left
            if next_index[0] == i - 1:
                self.cells[i][j].has_left_wall = False
                self.cells[i - 1][j].has_right_wall = False
            # down
            if next_index[1] == j + 1:
                self.cells[i][j].has_bottom_wall = False
                self.cells[i][j + 1].has_top_wall = False
            # up
            if next_index[1] == j - 1:
                self.cells[i][j].has_top_wall = False
                self.cells[i][j - 1].has_bottom_wall = False

            # recursively visit the next cell
            self.break_walls(next_index[0], next_index[1])
