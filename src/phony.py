from src.item import Item


class Phone(Item):
    """
    Класс для представления телефонов в магазине
    """

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса phone.

        :param name: Название телефона
        :param price: Цена за единицу
        :param quantity: Количество телефонов в магазине
        :param number_of_sim: Количество слотов для сим-карт в телефоне
        """

        super().__init__(name, price, quantity)
        self.__number_of_sim = None
        self.number_of_sim = number_of_sim

    @property
    def number_of_sim(self) -> int:
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim: int) -> None:
        """
        Устанавливает количество слотов для сим-карт в телефоне.

        Проверки:

        количество слотов должно быть целым числом больше нуля
        """
        if type(number_of_sim) is int and number_of_sim > 0:
            self.__number_of_sim = number_of_sim
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other):
        if isinstance(other, (self.__class__, self.__class__.__base__)):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя сложить эти объекты")