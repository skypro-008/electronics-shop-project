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

    def change_lang(self):
        """
        Функция, которая изменяет расклад с EN/RU
        и наоборот
        """
        if self.__language == "EN":
            self.__language = "RU"
        elif self.__language == "RU":
            self.__language = "EN"


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
