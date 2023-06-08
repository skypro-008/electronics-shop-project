"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item():
    return Item("test_PC", 35000, 4)


def test_init(test_item):
    assert test_item.name == "test_PC"
    assert test_item.price == 35000
    assert test_item.quantity == 4


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 140000


def test_apply_discount(test_item):
    test_item.pay_rate = 0.9
    test_item.apply_discount()
    assert test_item.price == 31500


def test_name(test_item):
    assert test_item.name == "test_PC"
    test_item.name = "test_notebook"
    assert test_item.name == "test_PC"


def test_initiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_item_string_to_number():
    assert Item.string_to_number('15') == 15
    assert Item.string_to_number("123456789098765") == 123456789098765
    assert Item.string_to_number('8.0') == 8
    assert Item.string_to_number('2.5') == 2


def test_repr(test_item):
    assert repr(test_item) == "Item('test_PC', 35000, 4)"


def test_str(test_item):
    assert str(test_item) == "test_PC"
