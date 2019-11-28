class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    """Create d-dimensional vector of zeros."""
    if type(d) == int:
      self._coords = [0] * d
    elif type(d) == list:
      self._coords = [0] * len(d)
      for i in range(len(d)):
        self._coords[i] = d[i]
    else:
      raise TypeError('constructor accepts dimension as int or list of coords')

  def __len__(self):
    """Return the dimension of the vector."""
    return len(self._coords)

  def __getitem__(self, j):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to given value."""
    self._coords[j] = val

  def __add__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    result = Vector(len(self))  # start with a vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result

  def __radd__(self, other):
    """Return sum of two vectors."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    result = Vector(len(self))  # start with a vector of zeros
    for j in range(len(self)):
      result[j] = self[j] + other[j]
    return result

  def __sub__(self, other):
    """Return subtraction of two vectors."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    result = Vector(len(self))  # start with a vector of zeros
    for j in range(len(self)):
      result[j] = self[j] - other[j]
    return result

  def __mul__(self, other):
    """Return product of two vectors."""
    result = Vector(len(self))  # start with a vector of zeros
    if type(other) == int or type(other) == float:
      for j in range(len(self)):
        result[j] = self[j] * other
      return result
    elif type(other) == Vector:
      if len(self) != len(other):
        raise ValueError('dimensions must agree')
      result = Vector(len(self))  # start with a vector of zeros
      for j in range(len(self)):
        result[j] = self[j] * other[j]
      return sum(result)
    else:
      raise TypeError('cannot multiply a vector by a ' + type(other).__name__)

  __rmul__ = __mul__

  def __eq__(self, other):
    """Return True if vector has same coordinates as other."""
    return self._coords == other._coords

  def __ne__(self, other):
    """Return True if vector differs from other."""
    return not self == other

  def __neg__(self):
    """Return a new vector whose coordinates are the negated values of the original coordinates."""
    result = Vector(len(self))  # start with a vector of zeros
    for j in range(len(self)):
      result[j] = -self[j]
    return result

  def __str__(self):
    """Produce string representation of vector."""
    return '<' + str(self._coords)[1:-1] + '>'


test1 = Vector(3)
test2 = Vector(3)

test1.__setitem__(0, 2)
test1.__setitem__(1, 3)
test1.__setitem__(2, 4)
test2.__setitem__(0, 5)
test2.__setitem__(1, 6)
test2.__setitem__(2, 7)

print(test1, test2)
print(test2 - test1)

print(-test1)

print(test1 + [1, 1, 1])
print([1, 1, 1] + test1)

print(test1 * 3)
print(3 * test1)
print(test1 * test1)

test3 = Vector([8, 9, 9])
print(test3)