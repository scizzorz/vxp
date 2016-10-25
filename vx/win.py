from . import editor
import curses

class Window:
  def __init__(self, cols, rows, x, y):
    self.window = curses.newwin(rows, cols, y, x)
    self.line = 1
    self.col = 1
    self.cols = cols
    self.rows = rows
    self.x = x
    self.y = y
    self.window.addch(0, 0, 'A')
    self.window.addch(rows-1, 0, 'B')
    self.window.addch(0, cols-1, 'C')
    self.window.addch(rows-2, cols-1, 'D')

  def focus(self):
    pass

  def print(self, text):
    pass

  def refresh(self):
    self.window.refresh()
