"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def my_object():
    item1 = Item('Смартфон', 10000, 20)
    return item1


def test_calculate(my_object):
    my_object.calculate_total_price()
    assert my_object.calculate_total_price() == 200000


def test_pay_rate(my_object):
    Item.pay_rate = 0.8
    my_object.apply_discount()
    assert my_object.price == 8000


def test_create_object(my_object):
    Item.pay_rate = 1.0
    assert my_object.price == 10000
    assert my_object.name == 'Смартфон'
    assert my_object.quantity == 20
    assert my_object.total_price == 0
    assert len(Item.all) != 0
    assert Item.pay_rate == 1.0
