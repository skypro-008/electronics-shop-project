from src.item import Item


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


# class Keyboard(Item):
#     def __init__(self, name: str, price: float, quantity: int, language: str):
#         super().__init__(name, price, quantity)
#         self.language = language
#
#     @property
#     def change_lang(self):
#         return self.language
#
#     @change_lang.setter
#     def change_lang(self, language):
        # if isinstance(number_of_sim, int) and number_of_sim > 0:
        #     return self.__number_of_sim
        # else:
        #     raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля')





# class Mixin_storage_warehousing():
#     storage = []
