from src.item import Item


class MixinLang:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__language = 'EN'

    def change_lang(self):
        """Изменяет язык (раскладку) клавиатуры.
        Доступные языки "EN", "RU" """
        if self.__language == 'EN':
            self.__language = 'RU'
        else:
            self.__language = 'EN'

    @property
    def language(self):
        """Возвращает язык клавиатуры"""
        return self.__language


class Keyboard(MixinLang, Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
