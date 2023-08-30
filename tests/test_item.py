import pytest

from src.item import Item
from src.settings import CSV

item1 = Item("Samsung Galaxy", 10000, 10)


def test_init():
    assert item1.name == "Samsung Galaxy"
    assert item1.price == 10000
    assert item1.quantity == 10


def test_calculate_total_price():
    assert item1.calculate_total_price() == 100000


def test_apply_discount():
    Item.pay_rate = 0.9
    item1.apply_discount()
    assert item1.price == 9000


def test_property_name():
    assert item1.name == "Samsung Galaxy"


def test_instantiate_from_csv():
    Item.instantiate_from_csv(CSV)
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
