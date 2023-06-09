import os
import csv


class InstantiateCSVError(Exception):
    """Класс исключения при повреждении файла CSV"""
    def __init__(self):
        self.message = 'Файл .cvs повреждён: не хватает колонок.'

    def __str__(self):
        return self.message


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name, price, quantity):
        """
        Инициализация экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self):
        """ Для отладки: выводит товар и его свойства """
        # "Item('Смартфон', 10000, 20)"
        return f"{__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        """Вывод элемента класса для пользователя"""
        # 'Смартфон'
        return f'{self.__name}'

    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Можно складывать только экземпляры классов Item')
        return self.quantity + other.quantity

    @property
    def name(self):
        """геттер для name"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """сеттер для name"""
        if len(new_name) > 10:
            raise Exception('Длина товара превышает 10 символов.')
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

    @classmethod
    def get_all_items(cls):
        """ Возвращаем список товаров """
        return cls.all

    @classmethod
    def get_count_items(cls):
        """ Подсчёт общего количества товаров """
        return len(cls.all)

    @classmethod
    def instantiate_from_csv(cls, path="../src/items.csv"):
        """ Создание объектов из данных файла """
        items = []

        try:
            with open(os.path.abspath(path), 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile, delimiter=',')
                required_columns = ['name', 'price', 'quantity']
                # Проверяем наличие необходимых колонок
                try:
                    if not all(column in reader.fieldnames for column in required_columns):
                        raise InstantiateCSVError()
                except InstantiateCSVError as e:
                    print(e)
                    raise
                else:
                    for row in reader:
                        try:
                            item = cls(row['name'], float(row['price']), int(row['quantity']))
                        except ValueError:
                            print(f"Ошибка при чтении данных в строке {reader.line_num}: {row}")
                            raise
                        else:
                            items.append(item)
        except FileNotFoundError:
            print("Отсутствует файл .csv")
            raise

        cls.all = items
        return cls.all

    @staticmethod
    def string_to_number(string):
        """ Перевод строки в число """
        return int(float(string))
