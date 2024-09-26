from src.item import Item


class MixinLang:
    """Класс-миксин для хранения и изменения раскладки клавиатуры"""
    LANG = 'EN'  # раскладка по умолчанию

    def __init__(self):
        """
        Языковая раскладка будет подтягиваться через объект-посредник
        при создании экземпляра класса Keyboard
        """
        self.__language = self.LANG

    @property
    def language(self):
        """Выводит раскладку клавиатуры"""
        return self.__language

    def change_lang(self):
        """Метод для изменения языка (раскладки клавиатуры)"""
        if self.language == "EN":
            self.__language = "RU"
        elif self.language == "RU":
            self.__language = "EN"
        return self


class Keyboard(Item, MixinLang):
    """
    Дочерний класс от Item для представления клавиатур в магазине.
    """

    def __init__(self, name: str, price: float, quantity: int, language: str = 'EN'):
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)
