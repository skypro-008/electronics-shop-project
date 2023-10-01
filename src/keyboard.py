import csv

class MixinLang:
    LANG = 'EN'

    def __init__(self):
        self._lang = self.LANG

    def change_lang(self):
        if self._lang == 'EN':
            self._lang = 'RU'
        elif self._lang == 'RU':
            self._lang = 'EN'
        else:
            raise ValueError(f"Unsupported language: {self._lang}")

    @property
    def language(self):
        return self._lang


class Keyboard(MixinLang):
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса Item.
        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return f'{self.__name}'

    def __add__(self, other):
        if isinstance(other, Keyboard):
            return self.quantity + other.quantity
        else:
            raise TypeError("Нельзя складывать разные типы товаров!")

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        if len(name) > 10:
            self.__name = name[:10]
        else:
            self.__name = name

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity * self.pay_rate

    def apply_discount(self, discount: float) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= discount

    def change_lang(self):
        """
        Метод для изменения языка клавиатуры.
        """
        super().change_lang()

        if self._lang not in {'EN', 'RU'}:
            raise ValueError(f"Unsupported language: {self._lang}")

    @classmethod
    def instantiate_from_csv(cls, filename: str) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла.
        :param filename: Имя файла.
        :return: None
        """

        with open(filename, newline='', encoding='utf-8') as csvfile:
            for row in csv.DictReader(csvfile):
                name = row['name']
                price = cls.string_to_number(row['price'])
                quantity = int(row['quantity'])
                item = cls(name, price, quantity)

    @staticmethod
    def string_to_number(string_value: str) -> float:
        return float(string_value)