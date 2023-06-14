"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def items():
    return Item('str', 200000, 20)


def test_item(items):
    assert items.name == 'str'
    assert items.price == 200000
    assert items.quantity == 20
    assert items.calculate_total_price() == 200000 * 20


def test_name(items):
    items.name = "Ноутбук"
    assert items.name == "Ноутбук"
    items.new_name = "Смартфон"
    assert items.new_name == "Смартфон"
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr():
    item = Item("Ноутбук", 32000, 15)
    assert repr(item) == "Item('Ноутбук', 32000, 15)"


def test_str():
    item = Item("Ноутбук", 32000, 15)
    assert str(item) == 'Ноутбук'

def test_add_class():
    item = Item("Ноутбук", 32000, 15)
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert item + phone == 20
    assert phone + phone == 10
    assert phone + 10 == Exception


def test_count_sim():
    phone = Phone("iPhone 14", 120000, 5, 2)
    assert phone.number_of_sim == 2
    count = phone.number_of_sim == 0
    assert count is False

    phone1 = Phone("iPhone 14", 120000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2

    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10