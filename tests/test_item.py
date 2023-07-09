"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
@pytest.fixture
def item():
    return Item("cake", 5.5, 3)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 16.5


def test_apply_discount(item):
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 4.4


def test_name(item):
    item.name = 'Table'
    assert item.name == 'Table'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5