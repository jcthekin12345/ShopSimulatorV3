class ConsoleView:
    """
    Provides a console-based user interface for interacting with a shopping system.

    This class contains methods to display various views, such as the main menu, available
    items, contents of the shopping cart, user balance, and messages. Additionally, it
    provides methods for capturing user input, such as menu choices and item selection.

    :ivar attribute1: Description of attribute1.
    :type attribute1: type
    :ivar attribute2: Description of attribute2.
    :type attribute2: type
    """
    def show_main_menu(self) -> str:
        print("\n=== Shop Menu ===")
        print("1. View items")
        print("2. View cart")
        print("3. Add to cart")
        print("4. Checkout")
        print("5. View balance")
        print("6. Exit")
        return input("Enter your choice (1-6): ")

    def show_items(self, items: list) -> None:
        print("\n=== Available Items ===")
        for item in items:
            print(f"ID: {item.item_id} | {item.name} | "
                  f"Price: ${item.price:.2f} | "
                  f"Stock: {item.quantity}")

    def show_cart(self, cart: list, total: float) -> None:
        print("\n=== Your Cart ===")
        for cart_item in cart:
            item = cart_item['item']
            quantity = cart_item['quantity']
            print(f"{item.name} x{quantity} - ${item.price * quantity:.2f}")
        print(f"\nTotal: ${total:.2f}")

    def show_balance(self, balance: float) -> None:
        print(f"\nYour balance: ${balance:.2f}")

    def get_item_choice(self) -> tuple:
        item_id = int(input("Enter item ID: "))
        quantity = int(input("Enter quantity: "))
        return item_id, quantity

    def show_message(self, message: str) -> None:
        print(f"\n{message}")