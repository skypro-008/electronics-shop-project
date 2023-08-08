"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item_data():
    item = Item("Смартфон", 10000, 20)
    return item


def test_item_calculate_total_price(item_data):
    assert item_data.calculate_total_price() == 200000


def test_item_apply_discount(item_data):
    item_data.pay_rate = 0.8
    item_data.apply_discount()
    assert item_data.price == 8000


def test_item_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item_data = Item.all[0]
    assert item_data.name == 'Смартфон'
    assert int(item_data.price) == 100
    assert int(item_data.quantity) == 1
def test_item_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_item_name(item_data):
    item_data.name = 'СуперСмартфон'
    assert item_data.name == "СуперСмарт"

def test_item_repr(item_data):
    assert repr(item_data) == "Item('Смартфон', 10000, 20)"
def test_item_srt(item_data):
    assert str(item_data) == 'Смартфон'

