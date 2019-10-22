def pair_product_odd(list):
  for i in list:
    for j in list:
      if (i + j) % 2 == 1:
        return True
  return False

print(pair_product_odd(list(range(10))))
print(pair_product_odd([8, 1, 2]))