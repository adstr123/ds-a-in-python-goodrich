def dot_product(listA, listB):
  return sum([i*j for (i, j) in zip(listA, listB)])

print(dot_product([1, 2, 3], [1, 3, 3]))