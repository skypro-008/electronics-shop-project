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
        self.__name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)
        self.all.append(self)

        # Геттер для name
        @property
        def name(self):
            """Возвращает наименование товара"""
            return self.name

        # Геттер для name
        @name.setter
        def set_name(self, quantity):
            """Метод срабатывает при операции присваивания. К наимерованию товара мы добавляем его колличество"""
            quantity, name = quantity.split(' ')
            self.quantity = quantity
            self.name = name



    @classmethod
    def instantiate_from_csv(cls) -> None:
        """Инициализирует экземпляры класса, получая объекты из csv файла"""
        cls.all.clear()
        try:
            with open(cls.CSV, newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    Item.all.append(cls(row['name'], row['price'], row['quantity']))
        except FileNotFoundError:
            print("Файл не найден")

    @staticmethod
    def string_to_number():
        return int(str)

    def calculate_total_price(self, price) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """

        return self.quantity * self.price

    def apply_discount(self, total_price=None, pay_rate=None) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        return self.price * self.pay_rate

    
