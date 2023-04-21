"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

def class_example_fixture_1():
    return Item("Чайник", 5000, 10)
def test_calculate_total_price():
    # pass
    assert Item("Чайник", 5000, 10).calculate_total_price() == 50000
    assert Item("Миксер", 3000, 3).calculate_total_price() == 9000
    assert Item("Пылесос", 15000, 3).calculate_total_price() == 45000

