import pytest
from src.item import Item
"""Здесь надо написать тесты с использованием pytest для модуля item."""


@pytest.fixture
def test_item1():
    return Item("Товар1", 100, 2)


@pytest.fixture
def test_item2():
    return Item("Товар2", 50, 3)


def test_repr(test_item1):
    assert test_item1.__repr__() == "Item('Товар1', 100, 2)"


def test_str(test_item2):
    assert test_item2.__str__() == 'Товар2'


def test_instantiate_from_csv(test_item_all):
    assert len(test_item_all) == 2


def test_calculate_total_price(test_item1):
    assert test_item1.calculate_total_price() == 200.0


def test_apply_discount(test_item1):
    Item.pay_rate = 0.8
    test_item1.apply_discount()
    assert test_item1.price == 80.0


def test_name(test_item1):
    test_item1.name = "Комп"
    assert test_item1.name == 'Комп'
    test_item1.name = "СуперКомпьютер"
    assert test_item1.name == 'СуперКомпь'


def test_string_to_number():
    assert Item.string_to_number('6.0') == 6
    assert Item.string_to_number('6') == 6
