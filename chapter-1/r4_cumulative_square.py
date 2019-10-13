def cumulative_square(limit):
  """Sums the square of all integers up to the given limit

  :param limit (int): exclusive limit of the cumulative squares
  :return: sum of the square of all integers up to limit
  """
  sum = 0
  for i in range(limit):
    sum += i**2

  return sum

print(cumulative_square(100))