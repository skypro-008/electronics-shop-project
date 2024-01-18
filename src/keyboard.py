from src.item import Item


class MixinLang:
    """
    Миксин класса Keyboard.
    """
    def __init__(self):

        self.__language = "EN"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """
        Меняет атрибут клавиатуры language (раскладку клавиатуры).
        """
        if self.language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'
        return self


class Keyboard(Item, MixinLang):
    """
    Класс для представления клавиатуры в магазине.
    """
    pass

################################################