"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


item1 = Item("Смартфон", 10000, 20)
item2 = Item('Ноутбук', 20000, 5)


def test_repr():
    assert item1.__repr__() == "Item('Смартфон', 10000, 20)"
    assert item2.__repr__() == "Item('Ноутбук', 20000, 5)"

def test_str():
    assert item1.__str__() == 'Смартфон'
    assert item2.__str__() == 'Ноутбук'

def test_item1():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000
def test_item1_price():
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0
    assert item2.price == 20000

def test_string_to_number():
    assert Item.string_to_number('7') == 7
    assert Item.string_to_number('7.6') == 7
    assert Item.string_to_number('7.4') == 7

def test_instantiate_from_csv():
    lists = Item.instantiate_from_csv()
    assert type(lists) == list