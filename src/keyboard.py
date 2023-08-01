from src.item import Item


class Mixin:
    """Класс содержит функционал для хранения и изменения раскладки клавиатуры"""

    def __init__(self):
        self.__language = "EN"

    @property
    def language(self):
        """Геттер для атрибута __language"""
        return self.__language

    def change_lang(self):
        """Метод изменяет раскладку клавиатуры"""

        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

        return self


class Keyboard(Item, Mixin):
    """Класс, описывающий сущность - клавиатура"""

    def __init__(self, name: str, price: float, quantiti: int) -> None:
        """Конструктор класса"""

        super().__init__(name, price, quantiti)
