from graphics import Window, Line, Point


class Cell:

    def __init__(self, canvas, point, width):
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.has_right_wall = True
        self.has_left_wall = True
        self.width = width
        self.center = Point(point.x, point.y)
        self.canvas = canvas
        self.visited = False

    def draw(self):
        l = self.width / 2
        # top_left = Point(self.center.x - l, self.center.y + l)
        # top_right = Point(self.center.x + l, self.center.y + l)
        # bottom_left = Point(self.center.x - l, self.center.y - l)
        # bottom_right = Point(self.center.x + l, self.center.y - l)
        bottom_left = Point(self.center.x - l, self.center.y + l)
        bottom_right = Point(self.center.x + l, self.center.y + l)
        top_left = Point(self.center.x - l, self.center.y - l)
        top_right = Point(self.center.x + l, self.center.y - l)

        if self.has_top_wall:
            self.canvas.draw_line(Line(top_left, top_right))
        else:
            self.canvas.draw_line(Line(top_left, top_right), 'white')
        if self.has_right_wall:
            self.canvas.draw_line(Line(top_right, bottom_right))
        else:
            self.canvas.draw_line(Line(top_right, bottom_right), 'white')
        if self.has_bottom_wall:
            self.canvas.draw_line(Line(bottom_right, bottom_left))
        else:
            self.canvas.draw_line(Line(bottom_right, bottom_left), 'white')
        if self.has_left_wall:
            self.canvas.draw_line(Line(bottom_left, top_left))
        else:
            self.canvas.draw_line(Line(bottom_left, top_left), 'white')

    def draw_move(self, target_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        self.canvas.draw_line(Line(self.center, target_cell.center), color)
