import pytest

from src.item import Item
from src.item import InstantiateCSVError
from src.phone import Phone
from src.settings import CSV

item1 = Item("Samsung", 10000, 10)
phone1 = Phone("IPhone", 100000, 15, 2)


def test_init():
    assert item1.name == "Samsung"
    assert item1.price == 10000
    assert item1.quantity == 10


def test_repr():
    assert repr(item1) == 'Item(Samsung, 10000, 10)'


def test_str():
    assert str(item1) == "Samsung"


def test_calculate_total_price():
    assert item1.calculate_total_price() == 100000


def test_apply_discount():
    Item.pay_rate = 0.9
    item1.apply_discount()
    assert item1.price == 9000


def test_property_name():
    assert item1.name == "Samsung"


def test_instantiate_from_csv():
    Item.instantiate_from_csv(CSV)
    assert len(Item.all) == 5
    assert Item.instantiate_from_csv("test") == FileNotFoundError


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_add():
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 30


def test_instantiate_from_csv_file_not_found():
    with pytest.raises(FileNotFoundError, match="Отсутствует файл item.csv"):
        Item.instantiate_from_csv("test")


def test_instantiate_from_csv_file_corrupted():
    with pytest.raises(InstantiateCSVError, match=InstantiateCSVError.FILE_CORRUPTED):
        Item.instantiate_from_csv("test")
