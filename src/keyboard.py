from src.item import Item


class LanguageMixin:
    __language = "EN"
    """
    Класс-mixin, обеспечивающий функциональные возможности переключения языка.
    """
    @property
    def language(self):
        """
        Геттер возвращает текущее значение
        """
        return self.__language

    def change_lang(self):
        """
        Если текущий язык — «EN», функция меняет его на «RU»,
        и наоборот.
        """
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self.__language


class Keyboard(Item, LanguageMixin):
    """
    Класс наследует параметры от классов Item, LanguageMixin
    """
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
