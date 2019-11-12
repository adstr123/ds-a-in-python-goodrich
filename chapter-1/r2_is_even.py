def is_even(k):
  """
  Takes an integer and returns True if it is even
  :param int k: the number to evaluate
  :return boolean: based on condition evaluation
  """
  # bitwise &
  # if last bit is 1, number is odd
  if k & 1:
    return False
  else:
    return True


"""
Time: O(1)
- Always one calculation that takes place
Space: O(1)
- Always needs 1 unit for input & 1 unit for return value
"""
