import pytest

from src.item import Item


@pytest.fixture
def item():
    return Item('', 0, 0)
