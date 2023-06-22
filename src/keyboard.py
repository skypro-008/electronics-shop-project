from src.item import Item


class Keyboard(Item):
    """
    Класс для товара “клавиатура”
    """

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Keyboard.
        :param name: Название клавиатуры.
        :param price: Цена за единицу клавиатуры.
        :param quantity: Количество клавиатур в магазине.
        """
        super().__init__(name, price, quantity)
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        if value in ['EN', 'RU']:
            self._language = value
        else:
            raise ValueError("Недопустимый язык. Допустимые значения: 'EN', 'RU'")

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = 'EN'
        return self

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"Keyboard('{self.name}', {self.price}, {self.quantity})"
