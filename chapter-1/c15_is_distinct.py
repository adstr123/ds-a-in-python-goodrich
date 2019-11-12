def is_distinct(integer_list):
  """Takes a list and determines if all elements are unique

  :param list integer_list: list of integers
  :return boolean: conditional on evaluation of the input
  """
  index = 0
  for i in integer_list:
    for j in integer_list:
      if i != index and i == j:
        return False
    index += 1
  return True


print(is_distinct(list(range(10))))
print(is_distinct(list([0, 1, 2, 3, 4, 5, 5, 6])))

"""
Time: O(n^2)
- n calculations per element in input (nested loops)
Space: O(n)
- 1 unit for external index, 2 units for loop indexing, 1 for return value
- Units required for integer_list grow with input size
- Both loops operate on the same list
"""
