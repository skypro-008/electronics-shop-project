"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_item():
    """
    Тестирование класса Item.
    """
    # Test case 1 # attributes
    item = Item('test_name', 1000, 5)
    assert item.name == 'test_name'
    assert item.price == 1000
    assert item.quantity == 5
    assert item.calculate_total_price() == 5000

    # Test case 2 # methods
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 500

    # Test case 3 # class variables
    assert len(Item.all) == 1
    item2 = Item('test_name2', 2000, 10)
    assert len(Item.all) == 2
