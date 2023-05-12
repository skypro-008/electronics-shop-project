from src.item import Item

class MixinLanguage:
    """
    Mixin-класс для метода change_lang
    """
    def __init__(self):
        self._language = "EN"

    def change_lang(self):
        """
        Метод для изменения языка клавиатуры
        """
        if self._language == "EN":
            self._language = "RU"
        elif self._language == "RU":
            self._language = "EN"
        return self

    @property
    def language(self):
        return self._language

class Keyboard(MixinLanguage, Item):
    """
    Класс Keyboard (наследование от MixinLanguage, Item)
    """

    def __init__(self, name: str, price: float, quantity: int):
        """
        Метод инициализации объекта класса Keyboard
        name: имя
        price: цена
        quantity: количество
        language: язык клавиатуры, по умолчанию EN
        """
        super().__init__()
        Item.__init__(self, name, price, quantity)
