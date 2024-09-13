import pytest
from src.item import Item

item = Item("Смартфон", 10000, 20)



@pytest.fixture
def item_fixture():
    return item
