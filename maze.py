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

    def test_draw(self):
        curr_cell = self.cells[0][0]
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                next_cell = self.cells[i][j]
                curr_cell.draw_move(next_cell)
