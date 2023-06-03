from src.item import Item


class LanguageMixin:
    """Создание миксина для смены раскладки языка"""
    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    @language.setter
    def language(self, value):
        raise AttributeError("property 'language' of 'KeyBoard' object has no setter")

    def change_lang(self):
        if self._language == "EN":
            self._language = "RU"
        elif self._language == "RU":
            self._language = "EN"
        return self


class Keyboard(Item, LanguageMixin):
    def __init__(self, name, price, quantity):
        """
        Инициализация экземпляра класса Keyboard.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__(name, price, quantity)
        super(LanguageMixin, self).__init__()
        self._language = "EN"
