from src.item import Item

class Phone(Item):
    """
    Создание экземпляра класса Phone.
    :param name: Название товара.
    :param price: Цена за единицу товара.
    :param quantity: Количество товара в магазине.
    :param number_sim: Количество сим карт
    """
    def __init__(self, name: str, price: float, quantity: int,number_of_sim) -> None:
        super().__init__(name, price,quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        """
        Возвращает значение(кол-во) сим карт
        """
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value) -> None:
        """
        Проверяет коичество сим-карт на 0 и флоат.
        При положительном результете выдает ошибку
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        self._number_of_sim = value
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'
