from src.item import Item


class MixinKeyboard:
    """
    Класс-миксин для хранения и изменения языка раскладки клавиатуры
    """
    LANGUAGE_EN = "EN"
    LANGUAGE_RU = "RU"

    def __init__(self):
        """
        Инициализатор класса Keyboard
        """
        self.language = self.LANGUAGE_EN

    def change_lang(self):
        """
        Метод меняет язык раскладки клавиатуры
        """
        if self.language == "EN":
            self.language = self.LANGUAGE_RU
        elif self.language == "RU":
            self.language = self.LANGUAGE_RU


class Keyboard(Item, MixinKeyboard):
    """
    Класс для товара Клавиатура
    """
    pass
