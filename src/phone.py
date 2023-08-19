from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: кол-во симкарт.
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __add__(self, other):
        """
        Сложение экземпляпов Phon и Item.
        Если переменная не является переменной экземпляров класса
        Phone и Item то сложения не происходит
        """
        if isinstance(other, Phone | Item):
            return int(self.quantity) + int(other.quantity)
        return "не является переменной экземпляров класса Phone и Item"

    def __radd__(self, other):
        """
        Сложение экземпляпов Phon и Item.
        Если переменная не является переменной экземпляров класса
        Phone и Item то сложения не происходит
        """
        if isinstance(other, Phone | Item):
            return int(self.quantity) + int(other.quantity)
        return "не является переменной экземпляров класса Phone и Item"

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {int(self.price)}, " \
               f"{int(self.quantity)}, {int(self.number_of_sim)})"
