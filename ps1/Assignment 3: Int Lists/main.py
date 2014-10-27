"""
"""

# Helper Code
def test():
  test_list = [3, 1, 4, 9, 9, 10, 2, 11, 4, 14, 5, 20, 21]
  assert get_min(test_list) == 1, "Expected min of 1"
  assert get_max(test_list) == 21, "Expected max of 21"
  assert get_median(test_list) == 9, "Expected median of 9"
  assert get_mode(test_list) == 9, "Expected mode of 9"
  assert get_floor(test_list, 25) == 21, "Expected floor of 21"
  assert get_ceil(test_list, 13) == 14, "Expected ceil of 14"

# Your Code

def get_min(nums):
  """Returns the smallest element in the list of numbers."""
  # TODO: Return the min element
  return 0

def get_max(nums):
  """Returns the largest number in the list of numbers."""
  # TODO: Return the largest number.
  return 0

def get_median(nums):
  """Returns the median number in the list."""
  # TODO: Return the median number
  return 0

def get_mode(nums):
  """Returns the most common number in the list.

  If there is a tie, return any of the most common numbers.

  """
  # TODO: Return the mode
  return 0

def get_floor(nums, val):
  """Returns the next smallest number in the list compared to val.

  If val is in the list, return val.

  """
  # TODO: Return the floor value
  return 0

def get_ceil(nums, val):
  """Returns the next largest number in the list compared to val.

  If val is in the list, return val.

  """
  # TODO: Return the ceil value
  return 0

def my_tests():
  # TODO: Write your own test cases here.
  pass

if __name__ == '__main__':
  test()
  my_tests()
