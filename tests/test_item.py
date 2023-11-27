"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def tv():
    return Item("tv", 10000, 2)


@pytest.fixture
def ctv():
    return Item("colortelevision", 15000, 3)


def test_item_initialization(tv):
    assert tv.name == "tv"
    assert tv.price == 10000
    assert tv.quantity == 2


def test_calculate_total_price(tv):
    tv.apply_discount()
    assert tv.calculate_total_price() == 20000.0


def test_apply_discount(tv):
    assert tv.apply_discount() is None


def test_name_property(ctv):
    assert ctv.name == "colortelevision"


def test_name_setter(ctv):
    ctv.name = ctv.name[0:10]
    assert ctv.name == "colortelev"


def test_name_property_1(tv):
    assert tv.name == "tv"


def test_instantiate_from_csv():
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
    assert Item.all[0].name == "Смартфон"
    assert Item.all[1].price == 1000
    assert Item.all[4].quantity == 5


def test_string_to_number_static():
    assert Item.string_to_number("5.76") == 5
