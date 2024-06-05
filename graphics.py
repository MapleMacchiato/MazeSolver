from tkinter import Tk, BOTH, Canvas


class Window:

    def __init__(self, width, height):
        self.root_widget = Tk()
        self.root_widget.title('Maze Solver')
        self.window = Canvas(self.root_widget, width=width,
                             height=height, bg='white')
        self.window.pack(fill=BOTH, expand=1)
        self.running = False
        self.root_widget.protocol('WM_DELETE_WINDOW', self.close)

    def redraw(self):
        self.root_widget.update_idletasks()
        self.root_widget.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
        print('Closing Window')

    def close(self):
        self.running = False
