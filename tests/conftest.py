import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000.0, 20)
