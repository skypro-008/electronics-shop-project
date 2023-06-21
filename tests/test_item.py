"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

@pytest.fixture
def exmp():
    return Item("Смарфтон", 10000, 20)

def calc(exmp):
    assert exmp.calculate_total_price() == 10000

def test_apply_discount(exmp):
    exmp.pay_rate = 0.8
    exmp.apply_discount()
    assert exmp.price == 8000