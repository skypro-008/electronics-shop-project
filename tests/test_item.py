"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_hm_1():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(test_hm_1):
    assert test_hm_1.calculate_total_price() == 200000


def test_init(test_hm_1):
    assert test_hm_1.price == 10000


def test_name(test_hm_1):
    assert test_hm_1.name == "Смартфон"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test__repr__(test_hm_1):
    assert repr(test_hm_1) == "Item('Смартфон', 10000, 20)"


def test__str__(test_hm_1):
    assert str(test_hm_1) == 'Смартфон'