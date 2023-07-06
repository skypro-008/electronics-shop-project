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
        self.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return

    def __repr__(self):
        return f"Item('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.__name


    @property
    def name(self):
        """
        Getter для получения значения атрибута name.
        """
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        """
        Setter для установки значения атрибута name.

        :param value: Новое название товара.
        """
        if len(value) > 10:
            self.__name = value[:10]
        else:
            self.__name = value
    @classmethod
    def instantiate_from_csv(cls):
        Item.all.clear()
        with open('../src/items.csv', 'r', encoding='windows-1251') as file:
            file_dict = csv.DictReader(file)
            for row in file_dict:
                Item(name=row['name'], price=row['price'], quantity=row['quantity'])


    @staticmethod
    def string_to_number(string_num):
        result = int(float(string_num))
        return result

