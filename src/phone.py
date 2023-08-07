from src.item import Item


class Phone(Item):
    def __init__(self, name, price, quantity, number_of_sim=1) -> None:
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    @property
    def number_of_sim(self):
        """ Возвращает имя товара"""
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, quantity):
        """Устанавливает новое количество SIM-карт"""
        if not isinstance(quantity, int) or quantity <= 0:
            print('ValueError: Количество физических SIM-карт должно быть целым числом больше нуля.')
        else:
            self.__number_of_sim = quantity



# if __name__ == '__main__':
#      item1 = Item("Смартфон", 10000, 20)
#      phone1 = Phone("iPhone 14", 120_000, 5, 2)
#      x = phone1 + phone1
#      print(item1 + item1)
#      phone1.number_of_sim = -1
#      print(phone1.number_of_sim)
