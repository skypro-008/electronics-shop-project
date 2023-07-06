"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def product_list_1():
    return Item("Пылесос", 25000, 5)


@pytest.fixture
def product_list_2():
    return Item("Плеер", 4000, 8)


@pytest.fixture
def product_list_3():
    return Item("Соковыжималка", 7500, 15)


def test_calculate_total_price(product_list_1):
    assert product_list_1.calculate_total_price() == 125000


def test_apply_discount(product_list_1):
    Item.pay_rate = 0.5
    product_list_1.apply_discount()
    assert product_list_1.price == 12500


def test_name(product_list_2):
    assert product_list_2.name == "Плеер"


def test_price(product_list_2):
    assert product_list_2.price == 4000


def test_quantity(product_list_2):
    assert product_list_2.quantity == 8


def test_string_to_number():
    assert Item.string_to_number('45841.84145') == 45841


def test_instantiate_from_csv():
    Item.all.clear()
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test__repr__(product_list_2):
    assert repr(product_list_2) == "Item(name=Плеер, price=4000, quantity=8)"


def test__str__(product_list_3):
    assert str(product_list_3) == "Соковыжималка"
