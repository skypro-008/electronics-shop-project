# -*- coding: utf-8 -*-
from src.item import Item

class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone. Содержит все атрибуты класса `Item` и дополнительно атрибут number_of_sim
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """
        Отображает информацию об объекте класса в режиме отладки
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        """
        Возвращает количество сим-карт
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """
        Проверяет, что количество сим-карт больше нуля
        """
        if value <= 0 or type(value) != int:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля")
        else:
            self.__number_of_sim = value