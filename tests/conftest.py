"""Conftest module"""
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
