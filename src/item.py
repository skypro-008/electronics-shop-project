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


    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv'):
        # В аргументы добавлен путь по умолчанию. В тестах вылетает ошибка, если не не менять путь
        Item.all = []
        with open(path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = row['price']
                quantity = row['quantity']
                cls(name, price, quantity)


    @staticmethod
    def string_to_number(string):
        return int(float(string))


    @property
    def name(self):
        """
        Возвращает наименование товара.
        """
        return self.__name


    @name.setter
    def name(self, name):
        """
        Проверка на длину наименования товара при инициализации
        """
        if len(name) <= 10:
            self.__name = name
        else:
            raise Exception("Длина наименования товара превышает 10 символов.")


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.

        :return: Стоимость товара с учетом скидки.
        """
        self.price *= Item.pay_rate
        return self.price
