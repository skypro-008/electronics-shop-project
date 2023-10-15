import pytest

from src.item import Item

@pytest.fixture
def make_item():
    return Item("Компьютер", 5000, 3)

def test_calculate_total_price(make_item):
    item = make_item
    assert item.calculate_total_price() == 15_000
    assert item.calculate_total_price() == item.price * item.quantity


def test_apply_discount(make_item):
    item = make_item
    first_price = item.price
    item.apply_discount()
    assert item.price == first_price * Item.pay_rate
    assert item.price == 5000.0

    item.price = first_price
    item.pay_rate = 1.2
    item.apply_discount()
    assert item.price == first_price * item.pay_rate
    assert item.price == 6000.0