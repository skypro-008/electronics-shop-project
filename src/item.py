""" Item Class module """
import csv
import os


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
        Initialize an Item instance.

        Args:
            name (str): The name of the item.
            price (float): The price of the item.
            quantity (int): The quantity of the item.

        Returns:
            None
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self) -> str:
        """
        Get the name of the item.

        Returns:
            str: The name of the item.
        """
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Set the name of the item.

        Args:
            name (str): The new name for the item.

        Raises:
            ValueError: If the length of the name exceeds 10 characters.

        Returns:
            None
        """
        if len(name) > 10:
            raise ValueError(
                "Длина наименования товара превышает 10 символов."
            )
        self.__name = name

    def calculate_total_price(self) -> float:
        """
        Calculate the total price of the item.

        Returns:
            float: The total price of the item.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Apply a discount to the item's price.

        Modifies the item's price by multiplying it by the pay rate.

        Returns:
            None
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Instantiate objects from a CSV file.

        Reads the CSV file 'items.csv' and creates instances of the class
        based on the data in the file.

        Returns:
            None
        """
        with open(
                os.path.join(
                    os.path.dirname(__file__),
                    'items.csv'
                ),
                'r',
                newline='',
                encoding="cp1251"
        ) as csvfile:
            data = csv.DictReader(csvfile)
            product: dict
            for product in data:
                cls(
                    product['name'],
                    cls.string_to_number(product['price']),
                    cls.string_to_number(product['quantity'])
                )

    @staticmethod
    def string_to_number(number: str) -> int:
        """
        Convert a string representation of a number to a numeric type.

        Args:
            number (str): String representation of a number.

        Returns:
            int: Numeric representation of the input number.
        """
        return int(float(number))
