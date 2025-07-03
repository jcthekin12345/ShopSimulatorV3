
class Item:
    """
    Represents an item in the inventory system.

    This class provides the structure for organizing item information such
    as its unique identifier, name, price, and quantity available. It also
    provides a method to convert the item's data into a dictionary format.

    :ivar item_id: The unique identifier of the item.
    :type item_id: int
    :ivar name: The name of the item.
    :type name: str
    :ivar price: The price of the item in the relevant currency.
    :type price: float
    :ivar quantity: The quantity of the item available in stock.
    :type quantity: int
    """
    def __init__(self, item_id: int, name: str, price: float, quantity: int):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_dict(self):
        return {
            'id': self.item_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }
