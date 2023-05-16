"""Тесты для модуля Item"""

from src.item import Item

"""Выводим стоимость товара"""

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

"""Устанавливаем скидку на товары"""
item1.pay_rate = 0.8
item2.pay_rate = 0.8

"""Применяем скидку на товары"""
item1.apply_discount()
item2.apply_discount()

assert item1.price == 16000.0
assert item2.price == 8000.0



