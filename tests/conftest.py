import pytest
from src.item import Item


@pytest.fixture()
def item_instance_kept():
    yield Item("", 0, 0)
    Item.all.clear()


@pytest.fixture()
def safe_item_class():
    Item.keep = False
    max_name_len = Item.max_name_len

    yield Item

    Item.keep = True
    Item.max_name_len = max_name_len
