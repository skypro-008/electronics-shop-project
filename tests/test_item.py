import export_parent_folder
from src.item import Item
import pytest

@pytest.fixture
def get_item1():
    return Item("Смартфон2", 20000, 15)
    
@pytest.fixture
def get_item2():
    return Item("Ноутбук2", 50000, 7)


def test_calculate_total_price(get_item1, get_item2):
    
    assert Item.calculate_total_price(get_item1) == 300000
    assert Item.calculate_total_price(get_item2) == 350000
    
def test_apply_discount(get_item1, get_item2):
    
    Item.pay_rate = 0.7
    Item.apply_discount(get_item1)
    Item.apply_discount(get_item2)
    assert get_item1.price == 14000
    assert get_item2.price == 35000
    
    Item.pay_rate = 0.0
    Item.apply_discount(get_item1)
    Item.apply_discount(get_item2)
    assert get_item1.price == 14000
    assert get_item2.price == 35000