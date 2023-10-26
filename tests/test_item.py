"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def items_fixture():
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    return item1, item2


def test_calculate_total_price(items_fixture):
    item1, item2 = items_fixture
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


def test_apply_discount(items_fixture):
    item1, item2 = items_fixture
    Item.pay_rate = 0.8
    item1.apply_discount()
    assert item1.price == 8000.0


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5.5


def test_name(items_fixture):
    item1, item2 = items_fixture
    item1.name = 'Смартфон'
    item2.name = 'СуперСмартфон'
    assert item1.name == 'Смартфон'
    if len(item1.name) <= 10:
        assert item1.name == 'Смартфон'
    else:
        assert item2.name == 'СуперСмарт'


def test__repr__(items_fixture):
    item1, item2 = items_fixture
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert repr(item2) == "Item('Ноутбук', 20000, 5)"


def test__str__(items_fixture):
    item1, item2 = items_fixture
    assert str(item1) == 'Смартфон'
    assert str(item2) == 'Ноутбук'
