def cumulative_square_odd(limit):
  return sum([x**2 for x in range(limit) if x % 2 == 0 and x > 0])

print(cumulative_square_odd(100))