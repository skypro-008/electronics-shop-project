from src.item import Item


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int) -> None:
        """
        Инициализация класса Phone и добавление метода super
        """
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    @property
    def number_of_sim(self):
        """
        Геттер для количества сим карт
        """
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, value):
        """
        Сеттер для количества сим карт
        """
        # if 0 < value < 2:
        #     self.__number_of_sim = int(value)
        # else:
        #     raise Exception('Количество физических SIM-карт должно быть целым числом больше нуля.')
        if value > 0 and value <= 2:
            self.__number_of_sim = int(value)
        else:
            raise Exception('Количество физических SIM_карт'
                            'должно быть целым числом больше нуля'
                            'и не больше двух')


# def __add__(self, other):
    """
    Реализуем метод сложения двух классов по количеству товара
    """
    # if isinstance(other, self.__class__):
    # #     return self.quantity + other.quantity
    # # return None
    # if issubclass(other.__class__, self.__class__):
    #     return self.__class__(self.quantity + other.quantity)
    # return None

    # if isinstance(other, Item):
    #     self.quantity += other.quantity
    #     return self
    # return None