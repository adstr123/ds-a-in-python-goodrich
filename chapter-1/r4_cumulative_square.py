def cumulative_square(limit):
  """Sums the square of all integers up to the given limit

  :param int limit: exclusive limit of the cumulative squares
  :return int: accumulation of the square of all integers up to limit
  """
  accumulation = 0
  for i in range(limit):
    accumulation += i ** 2

  return accumulation


print(cumulative_square(100))

"""
Time: O(n)
- One calculation per increment up to input
Space: O(1)
- One unit of space to track sum, one for loop index, one for return value
- One unit which is constantly increased, no matter the size of limit
"""
