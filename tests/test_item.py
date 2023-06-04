"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src import item
from src.item import Item


@pytest.mark.parametrize('price, quantity, expected', [
    (10000, 20, 200000),
    (20000, 5, 100000)
])
def test_calculate_total_price(price, quantity, expected):
    assert Item.calculate_total_price(price, quantity) == expected


def test_apply_discount():
    assert Item.apply_discount() == 10000
    assert Item.apply_discount() == 20000


def test_name('Смартфон'):
    assert isinstance(item, Item)
    assert item.name == 'Смартфон'


def test_name('СуперСмартфон'):
    assert isinstance(item, Item)
    assert item.name == 'Название товара не соответствует'


def test_instantiate_from_csv():
    assert len(Item.all) == 5


@pytest.mark.parametrize('number ,expected', [
    ('5', 5),
    ('5.0', 5),
    ('5.5', 5)
])
def test_string_to_number(number, expected):
    assert Item.string_to_number(number) == expected
