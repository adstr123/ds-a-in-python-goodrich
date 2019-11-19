class CreditCard:
  """A consumer credit card."""

  def __init__(self, customer, bank, acnt, limit):
    """Create a new credit card instance.
       The initial balance is zero.

    :param str customer: the name of the customer (e.g., John Bowman )
    :param str bank: the name of the bank (e.g., California Savings )
    :param str acnt: the acount identifier (e.g., 5391 0375 9387 5309 )
    :param int limit: credit limit (measured in dollars)
    """
    self._customer = customer
    self._bank = bank
    self._account = acnt
    self._limit = limit
    self._balance = 0

  def get_customer(self):
    """Return name of the customer."""
    return self._customer

  def get_bank(self):
    """Return the bank s name."""
    return self._bank

  def get_account(self):
    """Return the card identifying number (typically stored as a string)."""
    return self._account

  def get_limit(self):
    """Return current credit limit."""
    return self._limit

  def get_balance(self):
    """Return current balance."""
    return self._balance

  def charge(self, price):
    """Charge given price to the card, assuming sufficient credit limit.

    :param int/float price: the amount to add to the balance
    :return bool: True if charge was processed; False if charge was denied.
    """
    if not isinstance(price, (int, float)):
      raise TypeError('price must be numeric')

    if price + self._balance > self._limit:  # if charge would exceed limit
      return False                           # cannot accept charge
    else:
      self._balance += price
      return True

  def make_payment(self, amount):
    """Process customer payment that reduces balance.

    :param float amount: the amount to deduct from the balance
    """
    if not isinstance(amount, (int, float)):
      raise TypeError('amount must be numeric')
    if amount < 0:
      raise ValueError('amount must be positive')

    self._balance -= amount
