"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5.5

def test_name():
    item1.name = 'Смартфон'
    item2.name = 'СуперСмартфон'
    assert item1.name == 'Смартфон'
    if len(item1.name) <= 10:
        assert item1.name == 'Смартфон'
    else:
        assert item2.name == 'СуперСмарт'