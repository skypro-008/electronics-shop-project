"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def smartphone():
    return Item("Телевизор", 50000, 5)


def test_calculate_total_price(smartphone):
    item1 = Item("tea", 3000, 10)
    assert item1.price == 3000


def test_apply_discount():
    item1 = Item("tea", 3000, 10)
    item1.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 2400


def test___repr__(smartphone):
    assert repr(smartphone) == "Item('Телевизор', 50000, 5)"


def test___str__(smartphone):
    assert str(smartphone) == 'Телевизор'


