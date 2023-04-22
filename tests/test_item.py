"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

item3 = Item('Пылесос', 45000, 5)


def test_item_init():
    assert item3.name == "Пылесос"
    assert item3.price == 45000
    assert item3.quantity == 5


def test_calculate_total_price():
    assert item3.calculate_total_price() == 225000


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_apply_discount():
    Item.pay_rate = 0.8
    item3.apply_discount()
    assert item3.price == 36000


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name():
    item3.name = 'Смартфон'
    assert item3.name == 'Смартфон'


def test_verify_name():
    with pytest.raises(Exception):
        item3.name = 'СуперСмартфон'
        Item.verify_name(item3.name)
