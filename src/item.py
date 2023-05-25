from csv import DictReader
import os


class Item:
    """
    Класс для представления товара в магазине.
    """

    pay_rate = 1.0
    all = []
    path_to_cvs = os.path.join(os.path.dirname(__file__), "items.csv")

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """

        self.__name = None
        self.name = name

        self.__price = None
        self.price = price

        self.__quantity = None
        self.quantity = quantity

        self.all.append(self)

    def __repr__(self) -> str:
        """Возвращает строку, в которой перечислены свойства класса для просмотра в режиме отладки"""

        return f"{self.__class__.__name__}(\'{self.name}\', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """Возвращает строку с наименованием товара, рекомендовано для просмотра пользователем"""

        return f"{self.name}"

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """
        Устанавливает наименование товара.

        Проверки:

        наименование должно быть строкой
        длина наименования не должна превышать 10 символов
        """

        if not isinstance(name, str):
            raise ValueError("Наименование должно быть строкой")
        elif len(name) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = name

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float | int) -> None:
        """
        Устанавливает стоимость товара.

        Проверки:

        стоимость должна быть целым числом, либо вещественным
        """

        if type(price) not in (int, float):
            raise Exception("Цена должна быть числом")
        else:
            self.__price = float(price)

    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        """
        Устанавливает количество товара.

        Проверки:

        количество должно быть целым числом
        """

        if type(quantity) is not int:
            raise Exception("Количество должно быть выражено целым числом")
        else:
            self.__quantity = quantity

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

        if not isinstance(self.pay_rate, float):
            raise ValueError("Размер скидки задан неверно!")
        elif self.pay_rate > 1:
            raise ValueError("Размер скидки задан неверно!")
        else:
            self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        """
        Класс-метод для создания объектов класса в соответствии с характеристиками,
        указанными в csv-файле.
        Путь к файлу является атрибутом класса.
        """

        with open(cls.path_to_cvs) as csv_file:
            data_cvs = DictReader(csv_file)

            for row in data_cvs:
                name, price, quantity = row.values()
                price = cls.string_to_number(price)
                quantity = cls.string_to_number(quantity)
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(string):
        """Метод для превращения строки в формат числа: целого или с плавающей точкой"""

        if "." in string:
            try:
                number = float(string)
            except ValueError:
                raise ValueError("Нельзя превратить в число!")
            return number
        else:
            try:
                number = int(string)
            except ValueError:
                raise ValueError("Нельзя превратить в целое число!")
            return number|


#
