from src.item import Item


class MixIn:
    """Класс для обработки раскладки клавиатуры"""
    __language = "EN"

    def __init__(self):
        self.__language = "EN"

    def __str__(self):
        return f"{self.language}"

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> str:
        if self.language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"
        return self


class Keyboard(Item, MixIn):
    """Класс клавиатуры"""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """инициализация экземпляра класс"""
        super().__init__(name, price, quantity)

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity}, '{self.language}')"

    def __str__(self):
        return f"{self.name}"
