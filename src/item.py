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
        return self.__name


    @name.setter


    def name(self, new_name):
        if len(new_name) <= 10:
            self.__name = new_name
        else:
            self.__name = new_name[:10]


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

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла items.csv
        """

        cls.all = []

        import csv
        with open("items.csv", encoding = 'Windows - 1251') as r_file:

            file_reader = csv.reader(r_file, delimiter = ",")
            count = 0

            # Считывание данных из CSV файла
            for row in file_reader:
                if count != 0:
                    cls(row[0], float(row[1]), int(row[2]))
                count += 1


    @staticmethod


    def string_to_number(string: str) -> int:
        """
        Статический метод, возвращающий число из числа - строки
        :param string: строка, из которой нужно вернуть число
        :return: число
        """
        return int(float(string))
