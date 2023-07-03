"""Здесь надо написать тесты с использованием pytest для модуля item."""
from pytest import fixture
from src.item import Item
from src.phone import Phone

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

def test__repr__item(item):
    item1 = Item('Смартфон',10000,20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"

def test__str__item(item):
    item1 = Item('Смартфон',10000,20)
    assert str(item1) == 'Смартфон'

def test__repr__Phone(item):
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test__str__Phone(item):
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'

def test_adding_objs(item):
    item1 = Item("Смартфон", 10000, 20)
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10




