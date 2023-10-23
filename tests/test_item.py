"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item():
    return Item("TV", 10000, 5)


@pytest.fixture
def test__repr__():
    assert repr(test_item()) == "Item('Смартфон', 10000, 20)"


@pytest.fixture
def test__str():
    assert str(test__str()) == 'Смартфон'


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 50000


def test_apply_discount(test_item):
    test_item.pay_rate = 0.5
    test_item.apply_discount()
    assert test_item.price == 5000


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

