class User:
    """
    Represents a user in the system.

    This class contains information about a user, their attributes, and functionality
    to manage their shopping cart and balance. It allows adding items to a cart,
    computing cart totals, and checking or managing the user's balance.

    :ivar user_id: Unique identifier of the user.
    :type user_id: int
    :ivar username: Username associated with the user.
    :type username: str
    :ivar _balance: The current monetary balance of the user.
    :type _balance: float
    :ivar cart: List of items in the user's shopping cart with associated quantities.
    :type cart: list
    """
    def __init__(self, user_id: int, username: str, balance: float):
        self.user_id = user_id
        self.username = username
        self._balance = balance
        self.cart = []

    def add_to_cart(self, item: 'Item', quantity: int) -> bool:
        if quantity <= 0:
            return False
        self.cart.append({'item': item, 'quantity': quantity})
        return True

    def get_cart_total(self) -> float:
        return sum(item['item'].price * item['quantity'] for item in self.cart)

    def can_afford(self, amount: float) -> bool:
        return self._balance >= amount

    def deduct_balance(self, amount: float) -> bool:
        if self.can_afford(amount):
            self._balance -= amount
            return True
        return False

    @property
    def balance(self) -> float:
        return self._balance