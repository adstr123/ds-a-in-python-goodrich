def pair_product_odd(integer_list):
  """
  Take lists and determines if there is a distinct pair of elements whose product is odd.

  :param list integer_list: list of integers to check for pair products
  :return boolean: conditional on evaluation of the input
  """
  for i in integer_list:
    for j in integer_list:
      if (i + j) % 2 == 1:
        return True
  return False


print(pair_product_odd(list(range(10))))
print(pair_product_odd([8, 1, 2]))

"""
Time: O(n^2)
- n comparisons for each element in the input (nested loops)
Space: O(n)
- 2 units of space for loop indexing, 1 for return value
- Units of space for integer list grows with input size
- Doesn't need to double space as both loops operate on the same list and lists are referential
"""
