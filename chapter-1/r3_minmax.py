def minmax(data):
  """Takes a sequence of one or more numbers, and returns the smallest and largest numbers

  :param data (list): sequence of numbers
  :return (tuple): smallest & largest elements of data
  """
  minValue = data[0]
  maxValue = data[0]

  for num in data:
    if num < minValue:
      minValue = num
    if num > maxValue:
      maxValue = num

  return (minValue, maxValue)

print(minmax([1, 2, 6, 8, 9, 10]))
print(type(minmax([1, 2, 6, 8, 9, 10])))
