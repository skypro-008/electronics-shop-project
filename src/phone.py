from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim):
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, new_number):
        if new_number > 0 and self.is_int(new_number):
            self._number_of_sim = new_number
        else:
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")

    @staticmethod
    def is_int(digit):
        if digit == int(digit):
            return True
        else:
            return False


# if __name__ == '__main__':
#     phone1 = Phone("iPhone 14", 120_000, 5, 2)
#     print(phone1.quantity)
#     item1 = Item("Смартфон", 10000, 20)
#     print(item1.quantity)
#     print(phone1+item1)