import pytest

from src.phone import Phone


@pytest.fixture
def test_item():
    return Phone("iPhone 15", 110_000, 15, 2)


def test_init(test_item):
    assert test_item.name == "iPhone 15"
    assert test_item.price == 110000
    assert test_item.quantity == 15
    assert test_item.number_of_sim


def test_repr(test_item):
    assert repr(test_item) == "Phone('iPhone 15', 110000, 15, 2)"