import csv

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name : str, price: float, quantity: int) -> None:
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
        total_price = self.price * self.quantity
        return total_price
    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter

    def name(self, name):
        if len(name) <=10:
            self.__name = name
        else:
            print("Длина наименования превышает 10 символов")

    def instantiate_from_csv():
        with open('../src/items.csv', encoding='windows-1251') as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row['name'], row['price'])

    @staticmethod
    def string_to_number():
        return int(float())



