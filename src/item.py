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
        self.pay_rate = Item.pay_rate
        self.all.append(self)

    def __repr__(self) -> str:
        """Метод для отображения информации об объекте класса в режиме отладки (для разработчиков)"""
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"


    def __str__(self) -> str:
        """Метод для отображения информации об объекте класса для пользователей"""
        return f"{self.__name}"


    def __add__(self, other):
        if not isinstance(other, Item):
            raise ValueError('Складывать можно только объекты Item  и дочерние от ним')
        else:
            a = float(self.quantity)
            b = float(other.quantity)
            return int(a + b)

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
        self.price *= Item.pay_rate

    # Геттер для name
    @property
    def name(self):
        """Возвращает наименование товара. К атрибуту можно обращаться без вызова."""
        return self.__name

    # Cеттер для name
    @name.setter
    def name(self, name):
        """Сеттер проверяет, что длина наименования товара не больше 10 символов."""
        if len(name) <= 10:
            self.__name = name
            print(name)
        else:
            print("Длина наименования товара превышает 10 символов.")


    @classmethod
    def instantiate_from_csv(cls):
        cls.all.clear()
        filename = '../src/items.csv'

        try:
            with open(filename, 'r', encoding='cp1251', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    cls(row["name"], row["price"], row["quantity"])
        except FileNotFoundError:
            print('Файл не найден')

    @staticmethod
    def string_to_number(str_num):
        number = float(str_num)
        result = int(number)
        return result

item1 = Item("Смартфон", 10000, 20)
print(item1.calculate_total_price())