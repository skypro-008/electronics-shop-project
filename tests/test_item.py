"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
@pytest.fixture()
def item():
    item = Item("Смартфон", 10000, 20)
    return item
@pytest.fixture()
def phone():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone

def test_item_initialization(item):
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000

def test_string_to_number_1():
    string = "2"
    assert Item.string_to_number(string) == 2

def test_string_to_number_2():
    string = "2.3"
    assert Item.string_to_number(string) == 2

def test_apply_discount(item):
    assert Item.apply_discount(item) == 10000.0

def test_name_setter(item):
    item.name = 'FLŰGGÅƏNK∂€ČHIŒβØL∫ÊN'
    assert item._name == "FLŰGGÅƏNK∂"

def test__repr__(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"

def test__str__(item):
    assert str(item) == 'Смартфон'

def test__add__1(item,phone):
    assert item + phone == 25
    assert phone + phone == 10
    assert item + 10 == ValueError