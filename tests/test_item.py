"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def test_item():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 200_000


def test_apply_discount(test_item):
    Item.pay_rate = 0.5
    test_item.apply_discount()
    assert test_item.price == 5000


def test_name_getter(test_item):
    assert test_item.name == "Смартфон"


def test_name_setter(test_item):
    with pytest.raises(Exception):
        test_item.name = 'СуперСмартфон'


def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number(10) == 10
    assert Item.string_to_number('12586') == 12586



def test_setter_name(test_item):
    test_item.name = "Тестфон"
    assert test_item.name == "Тестфон"


def test___str__(test_item):
    assert str(test_item) == 'Смартфон'


def test___repr__(test_item):
    assert repr(test_item) == "Item('Смартфон', 10000, 20)"
