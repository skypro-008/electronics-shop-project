
from src.item import Item

class Phone(Item):
    """
    Класс для представления телефона в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, simq: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__(name, price, quantity)

        if not isinstance(simq, int) or simq < 1:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

        self.__number_of_sim = simq

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if number_of_sim >= 1:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        return


