from src.item import Item


class MixinLang:
    """
    Класс-миксин, который “подмешивает” в цепочку наследования класса `Keyboard` дополнительный функционал
    по хранению и изменению раскладки клавиатуры
    """
    def __init__(self):
        """
        Создание экземпляра класса MixinLang
        """
        self.__language = 'EN'

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Возвращает измененную раскладку клавиатуры
        Раскладка может быть только "RU" или "EN"
        """
        self.__language = ({"RU", "EN"} - {self.__language}).pop()
        return self


class Keyboard(Item, MixinLang):
    """
    Класс для представления клавиатур в магазине, созданный от классов Item и MixinLang.
    """
    pass
