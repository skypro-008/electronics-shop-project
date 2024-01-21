import pytest

from src.item import Item
from src.phone import Phone


@pytest.fixture
def item():
    return Item('', 0, 0)


@pytest.fixture
def phone():
    return Phone('', 0, 0, 0)
