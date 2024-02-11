from src.item import Item

class Phone(Item):
    """Класс для представления телефонов в магазине"""

    def __init__(self, name, price, quantity, number_of_sim):
        """Создание ээкземпляра класса Phone"""
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __repr__(self):
        """Отображает информацию об объектке класса"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self):
        """геттер для атрибута number_of_sim"""
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Сеттер для атрибута number_of_sim"""
        if isinstance(value, int) and value > 0:
            self._number_of_sim = value
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    def __add__(self, other):
        """Метод для сложения количества товаров"""
        if not isinstance(other, Item):
            raise ValueError("Экземпляр не принадлежит классу Item или Phone")
        return self.quantity + other.quantity
