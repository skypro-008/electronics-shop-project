"""Conftest module"""
import pytest

from src.item import Item


def item_class():
    """
    Create and configure item objects.

    Returns:
        tuple: A tuple containing two item objects.
    """
    phone = Item('iSung', 1500.50, 34)
    phone.pay_rate = 1.5
    console = Item('XStation', 987.50, 23)
    console.pay_rate = 0.5
    return phone, console


@pytest.fixture
def test_item():
    """
    Fixture that returns two instances of Item class for testing.

    Returns:
        tuple: A tuple containing two Item instances.
    """
    ent_1 = Item("Test1", 6.6, 65)
    ent_2 = Item("Test2", 196.0, 100)
    return ent_1, ent_2
