from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        """Инициализация класса с использованием атрибутов родительского класса и добавлением нового атрибута"""
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        """отображение информации об объекте класса в режиме отладки"""
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """Выводит кол-во сим-карт"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Записывает новое кол-во сим-карт с проверкой, что кол-во больше 0"""
        if value <= 0 or type(value) != int:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self.__number_of_sim = value