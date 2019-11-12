def dot_product(list_a, list_b):
  """Performs dot product on two lists

  :param list list_a: dot product left-hand side
  :param list list_b: dot product right-hand side
  :return int: dot product of input lists
  """
  return sum([i * j for (i, j) in zip(list_a, list_b)])


print(dot_product([1, 2, 3], [1, 3, 3]))

"""
Time: O(n)
- zip does one calculation per pairs of elements in inputs
- loop does one calculation per pairs of elements in inputs
- sum does one calculation per pairs of elements in inputs
Space: O(n)
- n units of space for zip result
- n units of space for loop result
- n units of space for sum result
"""
