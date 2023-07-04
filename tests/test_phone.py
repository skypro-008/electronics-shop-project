import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def cls_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def cls_item():
    return Item("Смартфон", 10000, 20)


def test_name(cls_phone):
    assert cls_phone.name == 'iPhone 14'


def test_repr(cls_phone):
    assert repr(cls_phone) == "Phone('iPhone 14', 120000, 5, 2)"
