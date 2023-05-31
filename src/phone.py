from src.item import Item


class Phone(Item):
    """
    Класс, представляющий телефон.
    Унаследован от класса Item.

    Атрибуты:
    name (str): название товара
    price (float): цена товара
    quantity (int): количество товара в наличии
    number_of_sim (int): количество физических SIM-карт
    """
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """ Для отладки: выводит товар и его свойства """
        # "Phone('iPhone 14', 120000, 5, 2)"
        return f"{__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __add__(self, other):
        if not isinstance(other, (Item, Phone)):
            raise ValueError('Можно складывать только экземпляры классов Item и Phone')
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        """Геттер для number_of_sim"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number):
        """
       Сеттер для number_of_sim.
       Проверяет, что значение нового количества SIM-карт больше нуля
       и является целым числом.
       Если проверка не пройдена, выводит сообщение об ошибке.
       """
        if not isinstance(new_number, int):
            raise ValueError('Количество физических SIM-карт должно быть целым числом.')
        elif new_number < 1:
            raise ValueError('Количество физических SIM-карт должно быть больше нуля.')
        else:
            self.__number_of_sim = new_number
