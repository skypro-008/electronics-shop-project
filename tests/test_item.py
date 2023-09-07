"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest
@pytest.fixture
def item():

    return Item("Смартфон", 100, 20)

def test_calculate_total_price(item):

    result = item.calculate_total_price()
    assert result==2000
def apply_discount(item):
    item.pay_rate = 0.7
    result = item.apply_discount()
    assert  result == 70
