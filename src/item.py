""" Item Class module """


class Item:
    """
    Class representing product in store.

    Class Attributes:
    ---------------
    pay_rate - discount rate (default: 1.0)
    all - list of all created entities

    Methods:
    ------------------
    calculate_total_price() - Calculates total price of specific
                                product in store
    apply_discount() - Applies set discount to specific product
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Create item class entity.

        :param name: product name.
        :param price: product price per unit.
        :param quantity: quantity of product in store.
        """
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Calculates total price of specific product in store

        :return: total product cost.
        :rtype: float
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Applies set discount to specific product
        """
        self.price *= self.pay_rate
