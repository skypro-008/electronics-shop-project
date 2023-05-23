"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def item():
    return Item("Принтер", 5299, 8)


def test_create_float(item):
    assert item.name == "Принтер"
    assert item.price == float(5299)
    assert item.quantity == 8
    assert item.pay_rate == 1.0


def test_create_int(item):
    assert item.name == "Принтер"
    assert item.price == 5299
    assert item.quantity == 8
    assert item.pay_rate == 1.0


def test_create_incorrect():
    with pytest.raises(ValueError):
        Item(8, 5299, 8)

    with pytest.raises(Exception):
        Item("Принтер Epson L121 (C11CD76414)", 5299, 8)

    with pytest.raises(Exception):
        Item("Принтер Epson L121 (C11CD76414)", "5299", 8)

    with pytest.raises(Exception):
        Item("Принтер Epson L121 (C11CD76414)", 5299, "8")


def test_price_incorrect(item):
    with pytest.raises(Exception):
        item.price = "18"


def test_quantity_incorrect(item):
    with pytest.raises(Exception):
        item.quantity = 19.6


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 5299 * 8


def test_apply_discount(item):
    item.pay_rate = 0.85
    item.price = 6000.0
    item.apply_discount()
    assert item.price == 0.85 * 6000.0


def test_apply_discount_incorrect(item):
    item.pay_rate = 2
    with pytest.raises(ValueError):
        item.apply_discount()

    item.pay_rate = 1.6
    with pytest.raises(ValueError):
        item.apply_discount()


def test_instantiate_from_csv():
    Item.all = []
    Item.instantiate_from_csv()
    assert Item.all[0].name == 'Смартфон'
    assert Item.all[3].price == 50.0
    assert Item.all[4].quantity == 5

    with pytest.raises(IndexError):
        print(Item.all[5])


def test_string_to_number_correct():
    assert Item.string_to_number("89") == 89
    assert type(Item.string_to_number("89")) is int

    assert Item.string_to_number("169.11") == 169.11
    assert type(Item.string_to_number("169.11")) is float


def test_string_to_number_incorrect():
    with pytest.raises(ValueError):
        Item.string_to_number("восемь")

    with pytest.raises(ValueError):
        Item.string_to_number("восемь.одиннадцать")


def test_repr(item):
    assert repr(item) == f"Item(\'{item.name}\', {item.price}, {item.quantity})"


def test_str(item):
    assert str(item) == f"{item.name}"
