from src.item import Item
import pytest


@pytest.fixture
def x():
    return Item('computer', 100, 10)


@pytest.fixture
def pay_rate():
    return 1.0


def test_item_init(x):
    assert x.name == 'computer'


def test_item_apply_discount(x, pay_rate):
    assert x.apply_discount(pay_rate) == 99


def test_item_calculate_total_price(x):
    assert x.calculate_total_price() == 1000

