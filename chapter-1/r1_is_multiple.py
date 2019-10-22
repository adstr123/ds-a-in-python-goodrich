def is_multiple(n, m):
  """
  Takes two numbers and returns True if the first is a multiple of the second
  :param n (int, float): total
  :param m (int, float): multiple candidate
  :return (bool): based on condition evaluation
  """
  if (n % m == 0):
    return True
  else:
    return False

  # Time: O(1)
  # Space: