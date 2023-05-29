"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, CSV_PATH


@pytest.fixture
def item():
    return Item("item1", 10.0, 5)


def test__repr__(item):
    assert repr(item) == "Item(item1, 10.0, 5)"


def test__str__(item):
    assert str(item) == "item1"


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 50.0


def test_apply_discount(item):
    item.pay_rate = 0.9
    item.apply_discount()
    assert item.price == 9.0


def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()

    assert len(items) == 4

    assert items[0].name == 'Ноутбук'
    assert items[0].price == 1000.0
    assert items[0].quantity == 3

    assert items[1].name == 'Кабель'
    assert items[1].price == 10.0
    assert items[1].quantity == 5


def test_all_items():
    item = Item("item1", 10.0, 5)

    assert item in Item.all


def test_string_to_number(item):
    """Тестируем преобразование числа из строки"""
    assert item.string_to_number("10000") == 10000
    assert item.string_to_number("3.024") == 3


def test_name_setter(item):
    """Тестируем сеттер """
    item2 = Item('samsung s10', 0.0, 0)
    item2.name = 'samsung s10'
    assert item2.name == 'samsung s10'


def test_name():
    item = Item("Test Items", 0.0, 0)
    item.name = "Test Item"
    assert item.name == "Test Item"

    item.name = "This is a very long name for an item"
    assert item.name == "Test Item"
    assert "Длинна наименования товара превышает 10 символов"
