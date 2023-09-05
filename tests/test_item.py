"""Здесь надо написать тесты с использованием pytest для модуля item."""
import csv
from csv import DictReader

import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.item import PATH_ABSOLUTE


@pytest.fixture()
def test_item():
    return Item(name="Phone", price=1000, quantity=10)


@pytest.fixture()
def test_phone():
    return Phone(name="iPhone 14", price=1000, quantity=1, number_of_sim=2)


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 10000


def test_apply_discount(test_item):
    test_item.pay_rate = 0.8
    test_item.apply_discount()
    assert 1000 * test_item.pay_rate == test_item.price


def test_string_to_number():
    assert Item.string_to_number("5") == 5
    assert Item.string_to_number("5.2") == 5
    assert Item.string_to_number("5.0") == 5


def test_name(test_item):
    item1 = test_item
    item1.name = "WIN"
    assert item1.name == "WIN"
    item1.name = "012345678910"
    assert len(item1.name) == 10
    assert item1.name == "0123456789"


def test_repr(test_item):
    assert repr(test_item) == "Item('Phone', 1000, 10)"


def test_str(test_item):
    assert str(test_item) == "Phone"


def test_add(test_item, test_phone):
    assert test_item + test_phone == 11
    assert test_phone + test_item == 11


def test_read_file():
    Item.instantiate_from_csv(PATH_ABSOLUTE)
    assert PATH_ABSOLUTE == '/home/stanislav/skypro_project/electronics-shop-project/src/items.csv'


def test_read_file_error():
    with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
        Item.instantiate_from_csv("not_file.csv")


def test_broken_file():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("test_items.csv")
        assert str(Item.instantiate_from_csv("test_items.csv")) == "Файл item.csv поврежден"

