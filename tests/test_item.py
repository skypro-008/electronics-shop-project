"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from random import randint, random
from src.item import Item


@pytest.mark.parametrize('name', [
    ("Ноутбук"),
    ("Смартфон")
])
def test_name_title(name):
    item = Item(name, randint(10000, 100000), randint(1, 100))
    assert item.name.istitle() == True


@pytest.mark.parametrize('name, price, quantity', [
    ('Смартфон', randint(10000, 100000), randint(1, 100)),
    ('Ноутбук', randint(10000, 100000), randint(1, 100))
])
def test_total_correct(name, price, quantity):
    item = Item(name, price, quantity)
    assert item.calculate_total_price() == price * quantity


@pytest.mark.parametrize('name, price, quantity, pay_rate', [
    ('Смартфон', randint(10000, 100000), randint(1, 100), random()),
    ('Ноутбук', randint(10000, 100000), randint(1, 100), random())
])
def test_apply_discount(name, price, quantity, pay_rate):
    item = Item(name, price, quantity)
    item.pay_rate = pay_rate
    assert item.apply_discount() == price * pay_rate


def test_name_property():
    name = "Laptop"
    new_name = "Macbook"
    long_name = "MacbookProfessional"
    item = Item(name, randint(10000, 100000), randint(1, 100))
    item.name = new_name
    assert item.name == new_name
    item.name = long_name
    assert item.name == long_name[:10]


def test_instantiate_from_csv():
    Item.all.clear()
    item = Item("Mac", randint(10000, 100000), randint(1, 100))
    assert len(item.all) == 1
    item.instantiate_from_csv('src/items.csv')
    assert len(item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

