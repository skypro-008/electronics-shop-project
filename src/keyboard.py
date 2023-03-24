
from src.item import Item

class Changer():
    """
    Класс для реализации смены раскладки клавиатуры
    """
    def __init__(self):
        self.__language = "EN"

    # @property
    # def language(self):
    #     return self._language

    def get_lang(self):
        return self.__language

    def change_lang(self):
        self.__language = "RU" if self.__language == "EN" else "EN"
        return self


class Keyboard(Changer, Item):
    """
    Класс для представления клавиатуры в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Инициализация экземпляра класса Keyboard.
        """
        Item.__init__(self, name, price, quantity)
        Changer.__init__(self)

    @property
    def language(self):
        return self.get_lang()