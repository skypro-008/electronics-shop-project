from src.item import Item


class MixinLang:
    '''Миксин - хранение и замена раскладки
    param: language  - раскладка'''

    def __init__(self, name_: str, price: float, quantity: int):
        super().__init__(name_, price, quantity)
        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(MixinLang, Item):
    '''Класс потомок - клавиатуры
    '''

    def __init__(self, name_: str, price: float, quantity: int):
        super().__init__(name_, price, quantity)
