from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт
        """
        super().__init__(name, price, quantity)
        self._number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, name: str):
        try:
            if len(name) > 10:
                raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
            self._name = name
        except ValueError as exception:
            print(f'Exception: {exception}')

    def __add__(self, new_item):

        if isinstance(new_item, Phone):
            return Phone(self.quantity + new_item.quantity)

        elif isinstance(new_item, Item):
            return Item(self.quantity + new_item.quantity)

        else:
            raise TypeError('Нельзя сложить Phone или Item с экземплярами не Phone или Item классов.')

    def __repr__(self):
        return f"{self.__class__.__name__}('{self._name}', {self.price}, {self.quantity}, {self._number_of_sim})"

    def __str__(self):
        return self._name
