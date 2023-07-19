import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item('name', 16000, 10)
