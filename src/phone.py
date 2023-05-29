from src.item import Item


class Phone(Item):
    """
    Класс для представления телефона в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim


    def __repr__(self) -> str:
        """
        Вывод информации об объекте для разработчика (в режиме отладки)

        :return: Класс объекта с текущими атрибтами
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"


    @property
    def number_of_sim(self) -> int:
        """
        Возвращает количество SIM-карт.
        """
        return self.__number_of_sim


    @number_of_sim.setter
    def number_of_sim(self, number: int) -> None:
        """
        Проверка на количество SIM-карт
        """
        if number <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')
        self.__number_of_sim = number
