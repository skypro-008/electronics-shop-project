"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def item():
    item = Item("Смартфон", 10000, 20)
    return item


def test_calculated_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    assert item.price == 10000


def test_name(item):
    item.name = "СуперCмартфон"
    assert item.name == "CуперCмарт"


def test_instantiate_from_csv(item):
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5


def test_string_to_number(item):
    assert Item.string_to_number('6.5') == 6


def test___repr__(item):
    assert repr(item) == "Item('Смартфон', 10000, 20)"


def test___str__(item):
    assert str(item) == 'Смартфон'
