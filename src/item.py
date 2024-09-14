import os

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

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if len(new_name) > 10:
            self.__name = new_name[:10]
        else:
            self.__name = new_name

    @classmethod
    def instantiate_from_csv(cls, path):
        path = os.path.join(os.path.dirname(__file__), os.path.basename(path))
        with open(path, "r") as file:
            content = file.readlines()
            for item in content:
                item_list = item.rstrip("\n").split(",")
                if item_list[2].isalpha():
                    continue
                else:
                    Item.all.append(Item(item_list[0], item_list[1], item_list[2]))

    @staticmethod
    def string_to_number(num: str):
        return int(float(num))
