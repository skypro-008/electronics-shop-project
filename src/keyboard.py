import pytest

from src.item import Item

class MixinChangeLang:
    """Добавляем функционал - клавиатуру"""

    def __init__(self):
        self.__language = "EN"

    def change_lang(self):
        """Меняем раскладку клавиатуры"""

        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, value):
        raise AttributeError("property 'language' of 'Keyboard' object has no setter")


class Keyboard(Item, MixinChangeLang):
    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)

def test_language():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == 'Dark Project KD87A'
    assert str(kb.language) == 'EN'

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

    with pytest.raises(AttributeError):
        kb.language = "CH"


