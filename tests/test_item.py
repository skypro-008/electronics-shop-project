"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def item_obj() -> Item:
    """
    Create Item object.
    """
    return Item(name="Phone", price=19999.9, quantity=5)


def test_class_attributes():
    """
    Attrs test.
    """
    assert isinstance(Item.pay_rate, float)
    assert Item.pay_rate < 1
    assert isinstance(Item.all, list)


def test_init(item_obj):
    """
    __init__ test.
    """
    assert isinstance(item_obj.name, str)
    assert isinstance(item_obj.price, float)
    assert isinstance(item_obj.quantity, int)

def test_calculate_total_price(item_obj):
    """
    calculate_total_price method test.
    """
    assert item_obj.calculate_total_price() == 19999.9 * 5

def test_apply_discount(item_obj):
    """
    apply_discount method test.
    """
    item_obj.apply_discount()
    assert item_obj.price == round(19999.9 * 0.85, 2)
