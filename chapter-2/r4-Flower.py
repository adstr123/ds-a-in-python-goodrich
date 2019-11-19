class Flower:
  """A flower."""

  def __init__(self, name, petals, price):
    """
    Create a new Flower instance.
    :param str name: the name of the flower
    :param int petals: the number of petals the flower has
    :param float price: how much the flower costs
    """
    self._name = name
    self._petals = petals
    self._price = price

  def get_name(self):
    """
    :return str: name of the flower.
    """
    return self._name

  def get_petals(self):
    """
    :return int: number of petals the flower has.
    """
    return self._petals

  def get_price(self):
    """
    :return float: how much the flower costs.
    """
    return self._price

  def set_name(self, name):
    """
    Updates the name of the flower.

    :param str name: the new name.
    """
    self._name = name

  def set_petals(self, petals):
    """
    Updates the number of petals the flower has.

    :param int petals: the new number of petals.
    """
    self._petals = petals

  def set_price(self, price):
    """
    Updates how much the flower costs.

    :param float price: the new price.
    """
