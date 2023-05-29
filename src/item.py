import csv


class Item:
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
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)


    def __repr__(self) -> str:
        """
        Вывод информации об объекте для разработчика (в режиме отладки)

        :return: Класс объекта с текущими атрибтами
        """
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self):
        """
        Вывод информации об объекте для пользователя

         :return: Наименование товара
        """
        return self.name


    def __add__(self, other: object) -> int:
        """
        Сложение товара в магазине (строго по классу)

         :return: Количество товаров
        """
        if isinstance(other, self.__class__) or issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        raise Exception('Складывать можно только товары и телефоны')

    # Вариант для сложения строго в определенном классе
    # def __add__(self, other) -> int:
    #     """
    #     Сложение товара в магазине (строго по классу)
    #
    #      :return: Количество товаров
    #     """
    #     if self.__class__ == other.__class__:
    #         return self.quantity + other.quantity
    #     raise Exception('Складывать можно только экземпляры одного класса')


    @classmethod
    def instantiate_from_csv(cls, path='../src/items.csv') -> None:
        """
        Инициализация экземпляров класса Item из файла src/items.csv
        """
        # В аргументы добавлен путь по умолчанию. В тестах вылетает ошибка, если не менять путь
        Item.all = []
        with open(path) as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = int(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)


    @staticmethod
    def string_to_number(string: str) -> int:
        """
        Возвращает число из числа-строки

        :return: число класса int
        """
        return int(float(string))


    @property
    def name(self) -> str:
        """
        Возвращает наименование товара.
        """
        return self.__name


    @name.setter
    def name(self, name: str) -> None:
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
