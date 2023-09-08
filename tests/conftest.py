import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture()
def some_item():
    item = Item("Смартфон", 10000, 5)
    return item

@pytest.fixture()
def some_phone():
    phone = Phone("iPhone 14", 120000, 5, 2)
    return phone
