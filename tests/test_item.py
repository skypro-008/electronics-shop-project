"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def start_data():
    return Item("Пижама", 999.9, 10)

def test_Item(start_data):
    assert Item("Пижама", 999.9, 10).name == 'Пижама'

def test_calculate_total_price(start_data):
    assert start_data.calculate_total_price() == 999.9*10

def test_apply_discount(start_data):
    start_data.apply_discount()
    assert start_data.price == 999.9