class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    """Create d-dimensional vector of zeros."""
    self._coords = [0] * d

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

  def __sub__(self, other):
    """Return subtraction of two vectors."""
    if len(self) != len(other):
      raise ValueError('dimensions must agree')
    result = Vector(len(self))  # start with a vector of zeros
    for j in range(len(self)):
      result[j] = self[j] - other[j]
    return result

  def __eq__(self, other):
    """Return True if vector has same coordinates as other."""
    return self._coords == other._coords

  def __ne__(self, other):
    """Return True if vector differs from other."""
    return not self == other

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
