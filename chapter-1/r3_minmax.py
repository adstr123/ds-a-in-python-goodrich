def minmax(data):
  """Takes a sequence of one or more numbers, and returns the smallest and largest numbers

  :param list data: sequence of numbers
  :return tuple: smallest & largest elements of data
  """
  min_value = data[0]
  max_value = data[0]

  for num in data:
    if num < min_value:
      min_value = num
    if num > max_value:
      max_value = num

  return min_value, max_value


print(minmax([1, 2, 6, 8, 9, 10]))
print(type(minmax([1, 2, 6, 8, 9, 10])))

"""
Time: O(n)
- One comparison per element in n, time taken to perform that comparison grows with n
Space: O(n)
- Always needs 2 units for min/max memory, 1 unit for loop index, 2 units for return values
- Units for n elements in data scales with data
"""
