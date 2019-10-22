def is_even(k):
  """
  Takes an integer and returns True if it is even
  :param k (int): the number to evaluate
  :return (boolean): based on condition evaluation
  """
  # bitwise &
  # if last bit is 1, number is odd
  if (k&1):
    return False
  else:
    return True