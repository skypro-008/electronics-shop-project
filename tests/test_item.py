"""Здесь надо написать тесты с использованием pytest для модуля item."""


import pytest

from src.item import Item



if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("НоутбукЛалал", 20000, 5)
    item3 = Item('Телефон', 10000, 5)

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
    item1 = Item('Смартфон',100,1)
    item2 = Item('НоутбукЛал', 200, 3)
    # длина наименования товара меньше 10 символов
    assert item1.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    assert item2.name == 'НоутбукЛал'
    # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr():
    item5 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item3 = Item('Телефон', 10000, 5)
    assert repr(item5) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"
    assert repr(item3) == "Item('Телефон', 10000, 5)"
def test_str():
    item5 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    item3 = Item('Телефон', 10000, 5)
    assert str(item5) == 'Смартфон'
    assert str(item2) == 'Ноутбук'
    assert str(item3) == 'Телефон'