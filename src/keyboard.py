from src.item import Item


class MixinKeyLang:
    """Класс миксин для ввода раскладки клавиатуры"""
    def __init__(self):
        self.__language = "EN"
    @property
    def language(self):
        """Реализация сеттера для language"""
        return self.__language

    @language.setter
    def language(self, value):
        """Сеттер для language"""
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter.")


    def change_lang(self):
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"
        return self






class KeyBoard(Item, MixinKeyLang):

    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

