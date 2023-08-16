"""Здесь надо написать тесты с использованием pytest для модуля item."""


import pytest

from src.item import Item

#item_1 = Item('Ноутбук', 1000, 3)
#item_2 = Item('Смартфон', 100, 1)
#item_3 = Item('Кабель', 10, 5)

#for item in Item.all:
    #print(f'{item.name}\n{item.calculate_total_price()} руб\nЦена со скидкой - {item.apply_discount()}\n')

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

def test_calculate_total_price():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000

def test_apply_discount():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    # устанавливаем новый уровень цен
    Item.pay_rate = 0.8
    # применяем скидку
    item1.apply_discount()

    assert item1.price == 8000.0
    assert item2.price == 20000

def test_length_of_the_name():
    pass
