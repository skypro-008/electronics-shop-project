from src.item import Item


class MixinLang:
    """
    Класс для изменения языка клавиатуры.
    """

    def __init__(self) -> None:
        self.__language = "EN"

    @property
    def language(self) -> str:
        """
        Возвращает значение __language.
        """
        return self.__language

    def change_lang(self) -> None:
        """
        Изменяет язык клавиатуры.
        """
        if self.__language == "RU":
            self.__language = "EN"
        else:
            self.__language = "RU"


class Keyboard(Item, MixinLang):
    """
    Класс для товара 'клавиатура'.
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        MixinLang.__init__(self)
