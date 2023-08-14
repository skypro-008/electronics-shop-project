"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item
from tests import test_phone


@pytest.fixture
def item() -> Item:
    return Item("Смартфон", 1000, 2)


def test_item_initialized(item) -> None:
    assert item.name == "Смартфон"
    assert item.price == 1000
    assert item.quantity == 2


def test_calculate_total_price(item) -> None:
    assert item.calculate_total_price() == 2000


def test_apply_discount(item) -> None:
    Item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 800


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_repr():
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"


def test_str():
    item1 = Item("Смартфон", 10000, 20)
    assert str(item1) == 'Смартфон'