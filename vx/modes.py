class Mode:
  def __init__(self, name):
    self._name = name

  def __eq__(self, other):
    return self._name == other._name

  def __ne__(self, other):
    return self._name != other._name

  def __str__(self):
    return self._name.upper()

  def __repr__(self):
    return '<Mode {}>'.format(self._name.upper())

class ModeTable:
  def __init__(self):
    self._modes = {}

  def __getattr__(self, key):
    return self._modes[key]

  def add(self, name):
    self._modes[name] = Mode(name)

  def __str__(self):
    return 'ModeTable'

  def __repr__(self):
    return '<ModeTable>'

modes = ModeTable()
modes.add('normal')
mode = modes.normal
