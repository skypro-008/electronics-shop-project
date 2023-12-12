from typing import Any

from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество сим-карт в телефоне.
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self) -> str:
        """
        Предоставляет информацию об объекте для разработчика.
        """
        return f"{self.__class__.__name__}('{super().get_name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self) -> int:
        """
        Возвращает значение атрибута '_number_of_sim'.
        """
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, num: int) -> Any:
        """
        Записывает атрибут '_number_of_sim'.
        """
        if isinstance(num, int) and num > 0:
            self._number_of_sim = num
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
