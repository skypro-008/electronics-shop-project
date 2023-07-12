import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def item():
    return Item("cake", 5.5, 3)


def test_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120_000, 5, 2)"


def test_add(phone, item):
    assert phone + item == 8




