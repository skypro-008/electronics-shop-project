from src.item import Item


class MixinLog:
    def change_lang(self):
        if self.language == 'EN':
            self.__language = 'RU'
        elif self.language == 'RU':
            self.__language = 'EN'
        else:
            raise ValueError('Неподдерживаемый язык. Поддерживаемые языки: EN, RU')


class Keyboard(Item, MixinLog):
    def __init__(self, name: str, price: float, quantity: int, language='EN'):
        super().__init__(name, price, quantity)
        self.__language = language

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, '{self.__language}')"

    def __str__(self):
        return f"{self.name}"

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        if self.__language == 'EN':
            self.__language = 'RU'
        elif self.__language == 'RU':
            self.__language = 'EN'
        else:
            raise ValueError('Неподдерживаемый язык. Поддерживаемые языки: EN, RU')