"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item1_2():
    Item.pay_rate = 1.1
    return Item("Декстоп", 400000, 2), Item("Клавиатура", 5000, 5)


def test_calculate_total_price(item1_2):

    assert item1_2[0].calculate_total_price() == 800000
    assert item1_2[1].calculate_total_price() == 25000


def test_apply_discount(item1_2):

    assert int(item1_2[0].apply_discount()) == 440000
    assert int(item1_2[1].apply_discount()) == 5500

def test_item_all():
    # можно сравнить по типам объектов? как?
    pass
