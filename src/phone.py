from src.item import Item

class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other):
        """ Переопределяет метод сложения количества товаров"""
        if not isinstance(other, self.__class__):
            raise ValueError("Невозможно сложить разные товары")
        return self.quantity + other.quantity

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        """ Добавляет проверку передаваемого значения"""
        if number < 0 or not isinstance(number, int):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше или равно нулю.")
        else:
            self._number_of_sim = number
