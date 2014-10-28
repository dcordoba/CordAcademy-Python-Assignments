"""Simulates moving a chess piece along a board."""
# Helper Code

class Position():
  def __init__(self, x=0, y=0):
    self.x = x
    self.y = y

  def __str__(self):
    return "(%s, %s)" % (self.x, self.y)

  def __repr__(self):
    return "(%s, %s)" % (self.x, self.y)

  def __eq__(self, other):
    return (isinstance(other, self.__class__)
      and self.x == other.x and self.y == other.y)

  def __ne__(self, other):
    return not self.__eq__(other)

class Size():
  def __init__(self, width=0, height=0):
    self.width = width
    self.height = height

def test():
  # Test valid moves within the board
  moves = ['RIGHT', 'DOWN', 'DOWN']
  start_position = Position(x=1, y=1)
  board_size = Size(width=3, height=4)
  expected_position = Position(x=2, y=3)
  end_position = get_end_position(start_position, board_size, moves)
  assert end_position == expected_position, "Expected end: %s, got: %s" % \
    (expected_position, end_position)

  # Test moves that take the pawn off the board
  moves = ['RIGHT', 'RIGHT', 'DOWN']
  start_position = Position(x=0, y=1)
  board_size = Size(width=3, height=2)
  expected_position == None
  end_position = get_end_position(start_position, board_size, moves)
  assert end_position == expected_position, "Expected end %s, got: %s" % \
    (expected_position, end_position)

  print 'All tests passed!'

# Your Code
def get_end_position(start_position, board_size, moves):
  """Given a starting position, board_size and list of moves, return the ending
  position.

  """
  # TODO: Return the ending position
  return None

if __name__ == '__main__':
  test()
