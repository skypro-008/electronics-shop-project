import csv

#
# class Item:
#     """
#     Класс для представления товара в магазине.
#     """
#     pay_rate = 1.0
#     all = []
#     file_name = 'src/items.csv'
#     def __init__(self, name: str, price: float, quantity: int) -> None:
#         """
#         Создание экземпляра класса item.
#
#         :param name: Название товара.
#         :param price: Цена за единицу товара.
#         :param quantity: Количество товара в магазине.
#         """
#         self.__name = name
#         self.price = price
#         self.quantity = quantity
#
#     def calculate_total_price(self) -> float:
#         """
#         Рассчитывает общую стоимость конкретного товара в магазине.
#
#         :return: Общая стоимость товара.
#         """
#         total_cost = self.price * self.quantity
#         return total_cost
#
#     def apply_discount(self) -> None:
#         """
#         Применяет установленную скидку для конкретного товара.
#         """
#         self.price = self.price - self.price * self.pay_rate / 100
#         self.all.append(Item(self.__name, self.price, self.quantity))
#
#     @property
#     def fullname(self):
#         """Возвращает полное наименование товара"""
#         return self.__name
#
#     @fullname.setter
#     def fullname(self, __name):
#         """Проверяет длину наименования товара"""
#         if len(self.__name) < 10:
#             print(self.__name)
#         else:
#             print(self.__name[:11])
#
#     @classmethod
#     def instantiate_from_csv(cls, file_name):
#         with open(file_name)as r_file:
#             file_reader = csv.reader(r_file, delimiter=",")
#             for row in file_reader:
#                 return cls.all.append([row[0], int(row[1]), int(row[2])])
#
#     @staticmethod
#     def string_to_number(number):
#         return int(number)
