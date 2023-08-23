import pytest
from src.item import Item
"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def test_position():
    return Item('Smartphone', 550.00, 10)


def test_calculate_total_price(test_position):
    assert test_position.calculate_total_price() == 5500


def test_apply_discount(test_position):
    Item.pay_rate = 0.8
    test_position.apply_discount(Item.pay_rate)
    print(test_position)
    assert test_position.price == 440

def test_init_item(test_position):
    assert test_position.name == 'Smartphone'
    assert test_position.price == 550.00
    assert test_position.quantity == 10
