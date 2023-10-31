"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest
from src.phone import Phone
from src.keyboard import Keyboard



@pytest.fixture
def item():
    return Item("Смартфонвфывфывфывфыв", 100, 20)


def test_calculate_total_price(item):
    result = item.calculate_total_price()
    assert result == 2000


def test_apply_discount(item):
    item.pay_rate = 0.7
    result = item.apply_discount()
    assert result == 70


def test_name(item):
    result = item.name
    assert result == 'Смартфонвфывфывфывфыв'


def test_name():
    item = Item("VeryLongNameThatExceedsMaxLength", 100, 20)
    assert len(item.name) >= 10


def test_string_to_number(item):
    result = item.string_to_number('6.8')
    assert result == 6


@pytest.fixture
def test_instantiate_from_csv(item):
    csv_date = {'name': 'dsadad'}
    result = item.instantiate_from_csv(csv_date)

    assert result.name == 'dsa'
def test_repr():
    item1 = Item("кандибобер на голове", 1000, 0)
    assert repr(item1) == "Item('кандибобер на голове', 1000, 0)"
def test_str():
    item1 = Item("кандибобер на голове", 1000, 0)
    assert str(item1)=='кандибобер на голове'

def test_repr_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_repr_phone():
    phone = Phone("кандибобер на голове", 1000, 0, 2)
    assert repr(phone) == "Phone('кандибобер на голове', 1000, 0, 2)"


def test_str_phone():
    phone = Phone("кандибобер на голове", 1000, 0,2)
    assert str(phone) == 'кандибобер на голове'


def test_add_phone():
    phone = Phone("кандибобер на голове", 1000, 10, 2)
    phone_1 = Item("кандибобер на голове", 1000, 15)
    assert phone + phone_1 == 25
    assert phone + phone == 20


def test_():
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"


