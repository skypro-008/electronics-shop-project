"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_phone():
    return Item("phone", 10000, 5)
def test_item_init1(item_phone):
    """Тестирует метод Item.__init__ с правильными значениями"""
    assert item_phone.get_name() == "phone"
    assert item_phone.price == 10000
    assert item_phone.quantity == 5

def test_item_init2():
    """Тестирует метод Item.__init__ с некорректным названием"""
    with pytest.raises(ValueError):
        Item(2, 2, 2)
    with pytest.raises(ValueError):
        Item("", 2, 2)


def test_item_init3():
    """Тестирует метод Item.__init__ с некорректным названием"""
    with pytest.raises(ValueError):
        Item("phone", "0.0", 2)
    with pytest.raises(ValueError):
        Item("phone", 0, 2)

def test_item_init4():
    """Тестирует метод Item.__init__ с некорректным названием"""
    with pytest.raises(ValueError):
        Item("phone", 1000, "asd")
    with pytest.raises(ValueError):
        Item("phone", 1000, 0)

def test_item_calc_tp(item_phone):
    """Тестирует Item.calculate_total_price()"""
    assert item_phone.calculate_total_price() == 50000

def test_item_apply_disc(item_phone):
    """Тестирует Item.apply_discount()"""
    Item.pay_rate = 0.7
    item_phone.apply_discount()
    assert item_phone.price == 7000