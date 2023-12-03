"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone
from src.keyboard import Keyboard

item_1 = Item("TV", 20000, 100)
Item.pay_rate = 2.0
phone1 = Phone("iPhone 14", 120_000, 5, 2)
# kb = Keyboard('Dark Project KD87A', 9600, 5)


def test_calculate_total_price():
    assert Item("TV", 20000, 100).calculate_total_price == 2000000
    assert Item("TV", 0, 100).calculate_total_price == 0


def test_apply_discount():
    item_1.apply_discount()
    assert 50000 * Item.pay_rate == float(100000)


def test_instantiate_from_csv():
    item_2 = Item("TV", 150, 2)
    assert isinstance(item_2, Item)
    assert item_2.name == 'TV'
    assert item_2.price == 150
    assert item_2.quantity == 2


def test_string_to_number():
    assert item_1.string_to_number('1000') == 1000


def test_name():
    item1 = Item.all[0]
    assert item1.name == 'TV'
    item_1.name = 'Smart TV'
    assert item_1.name == 'Smart TV'
    item_1.name = 'Smart Televizor'
    assert item_1.name == 'Smart Tele'


def test__repr__():
    assert repr(item_1) == "Item(TV,20000,100)"


def test__str__():
    assert str(item_1) == "TV"


def test__add__():
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_number_of_sim():
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone1.number_of_sim = -1


def test_repr_phone():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str_kb():
    assert str(kb) == "Dark Project KD87A"


def test_change_lang():
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"


def test_instantiate_from_csv1():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('qwerty.py')


def test_instantiate_from_csv2():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv('items(brake).csv')

