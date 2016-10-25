import curses

class Editor:
  def __init__(self):
    self.editing = True

    self.stdscr = curses.initscr()
    curses.start_color()
    curses.use_default_colors()

    '''
    for bg in range(16):
      for fg in range(16):
        curses.init_pair(bg*16 + fg + 1, fg, bg)
        '''

    curses.nonl()
    curses.raw()
    curses.noecho()

    self.stdscr.keypad(True)
    self.stdscr.clear()
    self.stdscr.refresh()

  def edit(self):
    while self.editing:
      code = self.stdscr.getch()
      self.key(code)

  def key(self, code):
    if code == ord('q'):
      self.quit()

  def quit(self):
    self.editing = False
    self.stdscr.keypad(False)

    curses.nl()
    curses.noraw()
    curses.echo()

    curses.endwin()
