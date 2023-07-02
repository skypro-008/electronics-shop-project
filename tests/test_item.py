"""Здесь надо написать тесты с использованием pytest для модуля item."""
from pytest import fixture
from src.item import Item

@fixture
def item():
    return Item("Смартфон", 10000, 20)

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000

def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 10000.0

def test_string_to_number(item):
    item.stroka = '3123 число'
    assert item.string_to_number(item.stroka) == 3123
    item.floatchislo = 5.0
    assert item.string_to_number(item.floatchislo) == 5
def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert len(Item.all) == 5





