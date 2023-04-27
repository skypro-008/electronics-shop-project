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

    @property
    def name(self):
        """
        Геттер для чтения приватного атрибута name
        """
        return self.__name

    @name.setter
    def name(self, name_len):
        """
        Сеттер проверяющий длину наименования товара
        В случае если наименование товара превышает 10 символов, то сеттер возвращает исключение:
        'Длина наименования товара превышает 10 символов.'
        """
        if len(name_len) > 10:
            raise Exception("Длина наименования товара превышает 10 символов.")
        else:
            self.__name = name_len

    @classmethod
    def instantiate_from_csv(cls, file):
        """
        Функция класс-метода для инициализации класса Item данными из файла
        """
        with open(file, 'r', encoding="cp1251") as csv_file:
            reader = csv.DictReader(csv_file)
            cls.all.clear()
            for i in reader:
                cls(i['name'], float(i['price']), int(i['quantity']))
            return cls.all

    @staticmethod
    def string_to_number(number):
        """
        Функция статик-метода которая преобразует число в формате Str/Float в формат Int
        """
        valid_number = int(float(number))
        return valid_number

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.pay_rate * self.price
        return self.price


