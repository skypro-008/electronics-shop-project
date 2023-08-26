from src.item import Item


class MixinLeng:
    language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"
        return self


class Keyboard(Item, MixinLeng):
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Keyboard.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param language: язык клавиатуры.
        """
        super().__init__(name, price, quantity)

    def __str__(self):
        return f"{self.name}"
