from src.item import Item

class MixinChangeLang:
    """Добавляем функционал - клавиатуру"""

    ch_lang = ('EN', 'RU')
    __slots__ = '__language'

    def __init__(self):
        self.__language = self.ch_lang[0]

    def change_lang(self):
        if self.language == self.ch_lang[0]:
            self.__language = self.ch_lang[1]
            return self
        elif self.language == self.ch_lang[1]:
            self.__language = self.ch_lang[0]
        return self

    @property
    def language(self):
        return self

    @language.setter
    def language(self, value):
        raise AttributeError("property 'language' of 'Keyboard' object has no setter")


class Keyboard(Item, MixinChangeLang):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)

    def test__repr__(self):
        assert Keyboard.__repr__(Keyboard('Dark Project KD87A', 9600, 5)) == "Keyboard('Dark Project KD87A', 9600, 5)"

    def test__str__(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5)
        assert str('Dark Project KD87A') == 'Dark Project KD87A'

    def test_language(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5, 'EN')
        assert str(kb.language) == 'EN'

    def test_change_lang(self):
        kb = Keyboard('Dark Project KD87A', 9600, 5, 'EN')
        kb.change_lang()
        assert str(kb.language) == "RU"


