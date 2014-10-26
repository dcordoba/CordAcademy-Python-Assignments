"""Simulates the flipping of a coin. When this program is run, a coin will be
flipped until 'HEADS' is achieved the given amount of tiems.

The flip_coin method is provided for you. You will use this method to 'flip' a
coin until you get the desired number of 'HEADS' in a row.

After each flip, you should print the result. Once we see the desired number of
'HEADS' in a row, print the total number of coin flips it took to get there and
exit the program.

"""
import random
import sys

# Starter Code

def flip_coin():
  """Simulates flipping a coin once.

  This method returns 'HEADS' 50% of the time, and 'TAILS' the other 50%.

  """
  sides = ['HEADS', 'TAILS']
  return random.choice(sides)

# Your code
def run_simulation(target_heads):
  print 'Flipping coin until we get %d HEADS' % target_heads
  # TODO: Use flip_coin to simulate flipping a coin until we get target_heads.


if __name__ == '__main__':
  """Parses the args and calls our run_simulation function."""
  assert len(sys.argv) > 1, "Missing the desired number of 'HEADS'"
  target_heads = int(sys.argv[1])
  run_simulation(target_heads)
