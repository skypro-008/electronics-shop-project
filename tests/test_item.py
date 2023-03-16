"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item



@pytest.fixture()
def item_1():
    return Item("Test1", 10000, 20)


@pytest.fixture()
def item_2():
    return Item("Test2", 20000, 30)


@pytest.fixture()
def item_from_csv():
    return Item.instantiate_from_csv()


def test_item_all():
    assert Item.all == []


def test_calculate_total_price():
    assert Item("Смартфон", 10000, 20).calculate_total_price() == 200000
    assert Item("Смартфон", 50000, 10).calculate_total_price() == 500000
    assert Item("Смартфон", 50000, 0).calculate_total_price() == 0


def test_apply_discount_1(item_1):
    Item.pay_rate = 0.8
    item_1.apply_discount()
    assert item_1.price == 8000.0


def test_apply_discount_2(item_2):
    Item.pay_rate = 0.9
    item_2.apply_discount()
    assert item_2.price == 18000.0


def test_string_to_number():
    assert Item.string_to_number('6') == 6
    assert Item.string_to_number('6.0') == 6
    assert Item.string_to_number('6.5') == 6
    assert Item.string_to_number('aaa') == 'Введено некорректное значение'


def test_instantiate_from_csv(item_from_csv):
    assert len(Item.all) == 5

