from src.item import Item


class MixinLanguage:
    """
    Класс-миксин, для изменения и хранения расклада
    клавиатуры
    """

    def __init__(self):
        self.__language = "EN"

    @property
    def language(self) -> str:
        return self.__language

    @language.setter
    def language(self, language: str):
        self.__language = language

    def change_lang(self):
        """
        Функция, которая изменяет расклад с EN/RU
        и наоборот
        """
        if self.language == "EN":
            self.language = "RU"
        elif self.language == "RU":
            self.language = "EN"


class Keyboard(Item, MixinLanguage):
    """
    Класс для товара 'клавиатура'
    """

    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
        MixinLanguage.__init__(self)

    def __str__(self):
        """
        Возвращает наименование товара
        """
        return self.name
