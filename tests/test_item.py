"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from pytest import fixture

from src.item import Item



@fixture
def item():
    return Item("Смартфон", 10000, 20)

def test_total_price(item):
    assert item.calculate_total_price() == 200000


def test_discount(item):
    item.apply_discount()
    assert item.price == 10000.0


def test_string_to_number(item):
    item.string_to_number('2')
    assert item.string_to_number(2) == 2


def test_instantiate_from_csv(item):
    item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_name(item):
    with pytest.raises(Exception):
        item.name = "knbknknelnblenwblnbl"

