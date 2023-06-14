from src.item import Item


class Phone(Item):
    """
    Класс для представления телефонов в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, sim_number: int):
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param sim_number: Количество симок в телефоне.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = sim_number

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        try:
            if value < 0 or int(value) != value:
                raise ValueError("# ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.")
            else:
                self.__number_of_sim = value
        except ValueError as e:
            print(e)

    def __repr__(self):
        """
        :return: Возвращает представление объекта для разработки
        """
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
