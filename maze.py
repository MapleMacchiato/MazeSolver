from cell import Cell
from graphics import Point
import time


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
            self.cells.append([])
            for y in range(self.num_rows):
                self.cells[x].append(Cell(
                    self.canvas,
                    Point(start_point.x + x*self.cell_width,
                          start_point.y + y*self.cell_width),
                    self.cell_width))

    def draw_cells(self):

        for r in range(self.num_cols):
            for c in range(self.num_rows):
                self.cells[r][c].draw()
                self.animate()

    def animate(self):
        self.canvas.redraw()
        time.sleep(0.02)
