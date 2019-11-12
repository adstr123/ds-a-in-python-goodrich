import math


def norm(v, p=2):
  """
  Calculates the p-norm of the given vector. A norm is a function that assigns a strictly positive length or size to each vector in a vector space. Defined as pth-root(v1^p + v2^p + ... + vn^p ) For the special case p=2 the Euclidian norm is given.
  :param v (list_to_reverse): numbers defining a vector
  :param p (int): p value to use as p-norm
  :return:
  """
  return sum([x ** p for x in v]) ** (1 / p)  # nth root of x == x^1/n


print(norm([4, 3]))
print(norm([4, 3], 2))
print(norm([4, 3, 9], 3))
