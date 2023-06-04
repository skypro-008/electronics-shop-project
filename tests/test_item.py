"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src import item
from src.item import Item


def test_calculate_total_price():
    assert item.Item("Смартфон", 10000, 20).calculate_total_price() == 200000
    assert item.Item("Ноутбук", 20000, 5).calculate_total_price() == 100000


def test_apply_discount():
    test_item = item.Item("Смартфон", 10000, 20)
    item.Item.pay_rate = 0.3
    test_item.apply_discount()
    assert test_item.price == 3000


def test_name():
    item1 = Item("Смартфон", 10000, 20)
    item1.name = "НеСмартфон"
    assert item1.name == 'НеСмартфон'

    item1.name = "СуперПуперМегаДрайвДваНеСмартфон"


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
