""" Phone class module """
from src.item import Item


class Phone(Item):
    """
    Class representing a phone.

    This class inherits from the Item class and extends it with additional
    attributes and methods specific to phones.

    Attributes:
        pay_rate (float): The discount rate for phones (default: 1.0).
        all (list): A list of all created phone objects.

    Methods:
        __init__: Initialize a Phone instance.
        __repr__: Return a string representation of the Phone object.
        number_of_sim: Get the number of SIM cards.
        number_of_sim.setter: Set the number of SIM cards.
        __add__: Add the quantities of two Phone objects.
    """

    def __init__(
        self,
        name: str,
        price: float,
        quantity: int,
        number_of_sim: int
    ) -> None:
        """
        Initialize a Phone instance.

        Args:
            name (str): The name of the phone.
            price (float): The price of the phone.
            quantity (int): The quantity of the phone.
            number_of_sim (int): The number of physical SIM cards.

        Returns:
            None
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self) -> str:
        """
        Return a string representation of the Phone object.

        Returns:
            str: The string representation of the Phone object.
        """
        return f"{self.__class__.__name__}('{self.name}', " \
               f"{self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """
        Get the number of SIM cards.

        Returns:
            int: The number of SIM cards.
        """
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value: int) -> None:
        """
        Set the number of SIM cards.

        Args:
            value (int): The new number of SIM cards.

        Raises:
            ValueError: If the value is less than or equal to 0.

        Returns:
            None
        """
        if value <= 0:
            raise ValueError(
                'Количество физических SIM-карт должно быть '
                'целым числом больше нуля.'
                )
        self._number_of_sim = value

    def __add__(self, other) -> int | None:
        """
        Add the quantities of two Phone objects.

        Args:
            other (Phone, Item): Another Phone or Item object to add.

        Returns:
            int: The sum of the quantities of the two Phone objects.
        """
        if issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        return None
