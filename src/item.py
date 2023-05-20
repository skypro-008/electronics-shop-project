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
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        """геттер для name"""
        if len(self.__name) <= 10:
            return self.__name
        return 'Наименование должно быть меньше 10 символов.'

    @name.setter
    def name(self, new_name):
        """сеттер для name"""
        self.__name = new_name

    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        if self.price < 0 or self.quantity < 0:
            return 'Проверьте товары. Цена или количество не должны быть отрицательными.'
        if self.price * self.quantity == 0:
            return 0
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.pay_rate = 0.8
        if self.price * self.pay_rate == 0.0:
            return 'Проверьте значения скидки или цены. Одно из них равно нулю.'
        if self.price * self.pay_rate < 0:
            return 'Проверьте значения скидки или цены. Одно из них меньше нуля'
        return self.price * self.pay_rate

    def __repr__(self):
        """ Для отладки: выводит товар и его свойства """
        return f'[Item: name={self.__name}, price={self.price}, quantity={self.quantity}]'

    @classmethod
    def get_all_items(cls):
        """ Возвращаем список товаров """
        return cls.all

    @classmethod
    def get_count_items(cls):
        """ Подсчёт общего количества товаров """
        return len(cls.all)

    @classmethod
    def instantiate_from_csv(cls):
        """ Создание объектов из данных файла """
        items = []
        with open('/home/fniad/PycharmProjects/electronics-shop-project/src/items.csv', 'r', newline='') as csvfile:
            reader = DictReader(csvfile)
            for row in reader:
                item = cls(row['name'], float(row['price']), int(row['quantity']))
                items.append(item)
        cls.all = items
        return cls.all

    @staticmethod
    def string_to_number(string):
        """ Перевод строки в число """
        return int(float(string))
