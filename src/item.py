""" Item Class module """
import csv
import os


class Item:
    """
    Class representing a product in a store.

    Class Attributes:
        pay_rate (float): The discount rate for products (default: 1.0).
        all (list): A list of all created item objects.

    Methods:
        __init__: Initialize an Item instance.
        __repr__: Return a string representation of the Item object.
        __str__: Return a string representation of the Item object.
        name: Get the name of the item.
        name.setter: Set the name of the item.
        calculate_total_price: Calculate the total price of the item.
        apply_discount: Apply a discount to the item's price.
        instantiate_from_csv: Instantiate objects from a CSV file.
        string_to_number: Convert a string representation of a number
        to a numeric type.
        __add__: Add the quantities of two Item objects.
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

    def __repr__(self) -> str:
        """
        Return a string representation of the Item object.

        Returns:
            str: The string representation of the Item object.
        """
        return f"{self.__class__.__name__}('{self.__name}', " \
               f"{self.price}, {self.quantity})"

    def __str__(self) -> str:
        """
        Return a string representation of the Item object.

        Returns:
            str: The string representation of the Item object.
        """
        return self.__name

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
                "Длина наименования товара превышает "
                "10 символов."
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
        """Convert a string representation of a number to a numeric type.

        Args:
            number (str): String representation of a number.

        Returns:
            int: Numeric representation of the input number.
        """
        return int(float(number))

    def __add__(self, other) -> int | None:
        """Add the quantities of two Item objects.

        Args:
            other (Phone, Item): The other Item or Phone object to add.

        Returns:
            int: The sum of the quantities of the two Item objects.
        """
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return None
