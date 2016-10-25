from . import win
import curses
import time

class Editor:
  def __init__(self):
    self.windows = []
    self.editing = True
    curses.wrapper(self.edit)

  def edit(self, stdscr):
    self.stdscr = stdscr

    curses.start_color()
    curses.use_default_colors()

    stdscr.clear()
    stdscr.refresh()

    while self.editing:
      self.refresh()
      code = self.stdscr.getch()
      self.key(code)
      time.sleep(0.1)

  def new_win(self, cols, rows, x, y):
    window = win.Window(cols, rows, x, y)
    self.windows.append(window)
    window.refresh()

    return window

  def key(self, code):
    if code == ord('q'):
      self.quit()

    if code == ord('a'):
      self.new_win(5, 5, len(self.windows)*6, 5)

  def refresh(self):
    for window in self.windows:
      window.refresh()

  def quit(self):
    self.editing = False
