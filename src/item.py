import csv


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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, newname):

        if len(newname) > 10:
            raise Exception(f'Длина наименования товара превышает 10 символов.')
        else:
            self.__name = newname

    @classmethod
    def instantiate_from_csv(cls):
        """
        Читает файл csv и берет нужные значения в класс, преобразуя строчные в числовые
        """
        with open("../src/items.csv", encoding="windows-1251") as file:
            file_csv = csv.DictReader(file, delimiter=",")
            data = []
            for i in file_csv:
                data.append(i)

        cls.all = []
        for i in data:
            cls(i['name'],
                cls.string_to_number(i['price']),
                cls.string_to_number(i['quantity'])
                )

    @staticmethod
    def string_to_number(num) -> int:
        """
        преобразует строчное значение в числовое int
        """
        if '.' in num:
            float_number = float(num)
            number = int(float_number)
        else:
            number = int(num)
        return number

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

