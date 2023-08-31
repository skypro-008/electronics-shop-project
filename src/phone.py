from src.item import Item


class Phone(Item):
    """класс Phone наследник Item"""

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        инициализация экземпляра класса
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: количество сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """Возвращает данные объекта"""
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """Геттер количества сим-карт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number_of_sim: int) -> None:
        """Сеттер количества сим-карт"""
        if new_number_of_sim <= 0 or not isinstance(new_number_of_sim, int):
            raise ValueError('There must be more than 0 sim cards in the phone.')
        else:
            self.__number_of_sim = new_number_of_sim
