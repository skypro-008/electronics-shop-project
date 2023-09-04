from src.item import Item


class MixinKeyboard:
    """
    Класс-миксин для хранения и изменения языка раскладки клавиатуры
    """

    def __init__(self, language="EN"):
        """
        Инициализатор класса Keyboard
        """
        self.__language = language

    def change_lang(self):
        """
        Метод меняет язык раскладки клавиатуры
        """
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"

        return self

    @property
    def language(self):
        """
        Геттер для language
        """

        return self.__language


class Keyboard(Item, MixinKeyboard):
    """
    Класс для товара Клавиатура
    """
    pass
