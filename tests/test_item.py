import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(item):
    assert item.calculate_total_price() == item.price * item.quantity


def test_apply_discount(item):
    item.apply_discount()
    assert item.price == 0.0


def test_all(item):
    assert item in Item.all
