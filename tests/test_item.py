import pytest
from src.item import Item

@pytest.fixture
def item():
    return Item('phone', 10000, 4)

def test_item_init(item):
    """Тестирование класса Item"""
    assert type(item.name) == str
    assert type(item.price) == int
    assert type(item.quantity) == int
    assert item.name == 'phone'
    assert item.price == 10000
    assert item.quantity == 4

def test_calculate_total_price(item):
    assert item.calculate_total_price() == 40000

def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 11000.0