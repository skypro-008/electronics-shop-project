from src.item import Item

LANG_LIST = ["EN", "RU"]


class Phone(Item):

    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.price}, {self.quantity}, {self.__number_of_sim})"

    def __str__(self):
        return f'{self.name}'

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity
        return ValueError

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number_of_sim):
        if type(number_of_sim) != int or number_of_sim <= 0:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')
        self.__number_of_sim = number_of_sim


class Mixin_storage_warehousing:
    """
    Mixin_storage_warehousing храним и изменению раскладки клавиатуры, “подмешивается”
    в цепочку наследования класса `Keyboard`
    """

    def __init__(self):
        self.__lang = "EN"

    def change_lang(self):
        """
        Изменение язык в LANG_LIST
        ко всему, что не соответствует текущему языку
        """
        for challenger in LANG_LIST:
            if self.__lang != challenger:
                self.__lang = challenger
                break
        return self

    @property
    def language(self):
        return self.__lang


class KeyBoard(Item, Mixin_storage_warehousing):
    pass
