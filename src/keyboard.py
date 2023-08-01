from src.item import Item


class MixinLang:

    """Класс для добавления возможности храения языка"""

    def __init__(self, name, price, quantity, language="EN"):
        super().__init__(name, price, quantity)
        self.__language = language

    def change_lang(self):

        """
        Функция изменения раскладки клавиатуры
        """

        if self.__language == 'EN':
            self.__language = 'RU'
            return self
        else:
            self.__language = 'EN'
            return self

    @property
    def language(self):
        return self.__language


class Keyboard(MixinLang, Item):

    pass
