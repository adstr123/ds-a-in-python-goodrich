def reverse_list(list_to_reverse):
  """

  :param list list_to_reverse: a list of arbitrary element type and length to reverse
  :return list: the reversed version of the input list
  """
  length = len(list_to_reverse)
  reversed_list = [None] * length
  for i in range(length):
    reversed_list[length - 1 - i] = list_to_reverse[i]
  return reversed_list


to_reverse = list(range(10))
print(reverse_list(to_reverse))

"""
Time: O(n)
- One assignment per element in the input list
Space: O(n)
- One unit of space to store length, one for loop indexing, one for return value
- Units required for input & reversed list to return grow with number of elements in input list
"""
