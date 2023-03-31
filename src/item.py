from csv import DictReader


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price * self.pay_rate
        self.quantity = quantity
        Item.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        if len(value) <= 10:
            print("Длина наименования товара меньше 10 символов")
            self.__name = value
        else:
            print("Длина наименования товара больше 10 символов")

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.quantity * self.price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, url='../src/items.csv'):
        cls.all.clear()
        with open(url, 'r', encoding='windows-1251') as file:
            file_reader = DictReader(file, delimiter=',')
            for value in file_reader:
                name, price, quantity = value.values()
                cls(name, cls.string_to_number(price), cls.string_to_number(quantity))

    @staticmethod
    def string_to_number(string):
        return int(float(string))

    def __add__(self, other):
        if isinstance(other, Item):
            return other.quantity + self.quantity
        else:
            raise ValueError("Сложение возможно только для экземпляров Item и Phone")

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {int(self.price)}, {self.quantity})"

    def __str__(self):
        return f'{self.name}'
