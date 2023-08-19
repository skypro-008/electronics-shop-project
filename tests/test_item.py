import pytest
from src.item import Item
# from src.item import calculate_total_price, apply_discount


@pytest.fixture
def item1():
    return Item('Lenovo', 50000, 5)


def test_item_quantity(item1):
    assert item1.quantity == 5


def test_item_name(item1):
    assert item1.name == 'Lenovo'


def test_item_price(item1):
    assert item1.calculate_total_price() == 250000


def test_apply_discount(item1):
    assert item1.apply_discount() == 50000


