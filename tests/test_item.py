from src.item import Item
import pytest

@pytest.fixture
def item1():
    item1 = Item("Часы", 16000, 30)
    return item1

def test_init(item1):
    assert item1.price == 16000
    assert item1.quantity == 30


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 480000


