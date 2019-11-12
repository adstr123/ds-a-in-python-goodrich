def is_multiple(n, m):
  """
  Takes two numbers and returns True if the first is a multiple of the second
  :param int/float n: total
  :param int/float m: multiple candidate
  :return (bool): based on condition evaluation
  """
  if n % m == 0:
    return True
  else:
    return False


"""
Time: O(1)
- Always one calculation that takes place
Space: O(1)
- Always needs 2 units for input & 1 unit for return value
"""
