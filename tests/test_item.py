"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


@pytest.fixture
def item1():
    return Item("Смартфон", 10_000, 20)


def test_init(item1):
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20
    assert Item.all[0] == item1


def test_calculate_total_price(item1):
    assert item1.calculate_total_price() == 200_000


def test_apply_discount(item1):
    old_price = item1.price
    item1.apply_discount()
    assert item1.price == old_price * Item.pay_rate


def test_class_attribute(item1):
    assert isinstance(Item.pay_rate, float)
    assert isinstance(Item.all, list)


def test_property_name(item1):
    assert item1.name == 'Смартфон'
    item1.name = 'Телефон'
    assert item1.name == 'Телефон'

    with pytest.raises(Exception, match=r'* 10 *'):
        item1.name = 'СуперСмартфон'


def test_instantiate_from_csv():
    Item.instantiate_from_csv()

    assert len(Item.all) == 5
    assert Item.all[1].name == 'Ноутбук'
    assert Item.all[1].price == '1000'
    assert Item.all[1].quantity == '3'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
    assert Item.string_to_number(None) == None
    assert Item.string_to_number('not_number') == None
