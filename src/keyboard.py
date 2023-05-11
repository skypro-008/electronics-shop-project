from src.item import Item

LANG_LIST = ["EN", "RU"]
class MixinStorageWarehousing:
    """
    MixinStorageWarehousing храним и изменению раскладки клавиатуры, “подмешивается”
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


class Keyboard(Item, MixinStorageWarehousing):


    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)