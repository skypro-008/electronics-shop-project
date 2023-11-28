"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def first_item():
    return Item("Лампа", 100, 10)


def test_apply_discount(first_item):
    Item.pay_rate = 0.8
    first_item.apply_discount()
    assert first_item.price == 80


def test_calculate_total_price(first_item):
    assert first_item.calculate_total_price() == 1000


def test_name_setter():
    item = Item("TVset", 50000, 1)
    assert item.name == "TVset"
    assert len(item.name) == 5


def test_instantiate_from_csv():
    csv_data = "Laptop,1500,2\nKabel,15,5\n"
    with open("test_item.csv", "w", encoding="utf-8") as csv_file:
        csv_file.write(csv_data)
