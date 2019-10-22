def reverse_list(list):
  length = len(list)
  reversed_list = [None] * length
  for i in range(length):
    reversed_list[length - 1 - i] = list[i]
  return reversed_list

to_reverse = list(range(10))
print(reverse_list(to_reverse))