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
        self.name = name
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
        self.price = self.price * self.quantity


    @property
    def name(self) -> str:
        """
        Возвращает название товара.

        :return: Название товара.
        """
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        """
        Устанавливает название товара.

        :param value: Новое название товара.
        """
        if len(value) > 10:
            self._name = value[:10]
        else:
            self._name = value

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
        self.price = self.price * self.pay_rate


    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv.
        """
        with open("items.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row["name"]
                price = cls.string_to_number(row["price"])
                quantity = cls(row["quantity"])
                item = cls(name, price, quantity)
                cls.all.append(item)

    @staticmethod
    def string_to_number(value: str) -> float:
        """
        Возвращает число из числа-строки.

        :param value: Число-строка.
        :return: Число.
        """
        return float(value)


if __name__ == '__main__':
    Item.instantiate_from_csv()
    item1 = Item("Смартфон", 10000, 20)
    print(Item.all)