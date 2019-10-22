def is_distinct(list):
  index = 0
  for i in list:
    for j in list:
      if (i != index and i == j):
        return False
    index += 1
  return True

print(is_distinct(list(range(10))))
print(is_distinct(list([0,1,2,3,4,5,5,6])))