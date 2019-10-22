def factors(n):
  k = 1
  while k * k < n:
    if n % k == 0:
      yield k
    k += 1
  k = 1
  while k * k < n:
    if n % k == 0:
      yield n // k
    k += 1
  if k * k == n:
    yield k


print(list(factors(100)))