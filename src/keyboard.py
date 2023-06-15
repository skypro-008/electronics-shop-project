from src.item import Item


class MixinLanguage:

    def __init__(self):
        self.__lang = 'EN'

    def change_lang(self):
        if self.__lang == 'RU':
            self.__lang = 'EN'

        else:
            self.__lang = 'RU'
        return self

    @property
    def language(self):
        return self.__lang


class Keyboard(Item, MixinLanguage):
    """
    Класс для представления клавиатур в магазине.
    """
    def __init__(self, name: str, price: float, quantity: int):
        """
        Создание экземпляра класса Keyboard.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        super().__init__(name, price, quantity)

    def __repr__(self):
        """
        :return: Возвращает представление объекта для разработки
        """
        return f"Keyboard ('{self.name}')"

