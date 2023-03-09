from src.item import Item
import pytest
"""Здесь надо написать тесты с использованием pytest для модуля item."""
@pytest.fixture
def name():
    return "iphone 5S"
@pytest.fixture
def price():
    return 20000.0
@pytest.fixture
def quantity():
    return 15

def test_Item(name, price, quantity):
    product = Item(name, price, quantity)
    Item.pay_rate = 0.85
    assert product.name == "iphone 5S"
    assert product.price == 20000.0
    assert product.calculate_total_price() == 300000
    product.apply_discount()
    assert product.price == 17000
