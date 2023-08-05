def nice_number_output(number) -> str:
    """
    возвращает красиво номер 100000.011 в виде "100 000.011'
    """
    result = ''
    str_number = str(number)
    # ищем точку в числе
    if str_number.count('.') > 0:
        is_dot = False
        index_dot = 0
        for i, str_n in enumerate(str_number[::-1]):
            result = str_n + result
            if is_dot:
                if (i - index_dot) % 3 == 0:
                    result = ' ' + result
            if str_n == '.':
                is_dot = True
                index_dot = i
    else:
        # точки нет - выводим число с пробелами
        for i, str_n in enumerate(str_number[::-1]):
            result = str_n + result
            if i % 3 == 2:
                result = ' ' + result

    return result


class Item:
    """
    Класс для представления товара в магазине.
    """
    # скидка на товар (100% - 15%)
    pay_rate = 0.85
    all = []

    def __init__(self, name: str, price: float, quantity=1) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине, по умолчанию 1
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
        return self.price*self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    def __repr__(self):
        """
        метод __repr___
        """
        return f"Item('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        """
        метод __str___
        """
        return f'{self.name} в количестве {self.quantity} шт ' \
               f'по цене {self.price} руб.'

# проверяем работу класса
# temp_item = Item('Молоко 3,5%', 95, 5)
# print(repr(temp_item))
# print(f'{temp_item}, Итоговая сумма = {temp_item.calculate_total_price()} руб.')
# print(f'Применяем скидку {int((1-temp_item.pay_rate)*100)}%')
# temp_item.apply_discount()
# print(repr(temp_item))
# print(f'{temp_item}, Итоговая сумма = {temp_item.calculate_total_price()} руб.')
# print(nice_number_output(10000000))
# print(nice_number_output(10000000.0111))
