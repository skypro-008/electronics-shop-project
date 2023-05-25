"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def start_data():
    return Item("Пижама", 999.9, 10)


def test_Item(start_data):
    assert start_data.name == 'Пижама'
    start_data.name = 'Шкаф'
    assert start_data.name == 'Шкаф'
    start_data.name = 'СлишкомДлинноеСлово'
    assert start_data.name == 'Шкаф'
    Item.instantiate_from_csv()
    assert len(Item.all) == 6
    assert start_data.string_to_number('50.1') == 50
    start_data.instantiate_from_csv()
    assert start_data.all[1].price == '100'


def test_calculate_total_price(start_data):
    assert start_data.calculate_total_price() == 999.9*10


def test_apply_discount(start_data):
    start_data.apply_discount()
    assert start_data.price == 999.9

