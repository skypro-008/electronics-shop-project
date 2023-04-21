

class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int):
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
    def instantiate_from_csv(cls):
        from csv import DictReader as read


    def set_name(self, name):
        if len(name) <= 10:
            self.__name = name
        raise Exception("Длина наименования товара превышает 10 символов")

    def get_name(self):
        return self.__name

    def calculate_total_price(self):
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price*self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price*self.pay_rate


    @staticmethod
    def string_to_number(str_num):
        try:
            return int(str_num)
        except ValueError:
            print("Это не число")