def factors(n):
  """Generator yields factors of input integer

  :param int n: integer to calculate factors for
  :return Iterator[int]: int yields from calculation
  """
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

"""
Time: O(n)
- one calculation & comparison per input element (incrementing while by 1, potentially leading to a yield)
Space: O(n)
- 1 unit each for k, n, yield value
- one unit of space per input element for first loop
- one unit of space per input element for second loop
"""
