import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone1():
    return Phone('iPhone 13', 100000, 7, 1)


def test_phone_init(phone1):
    assert phone1.name == 'iPhone 13'
    assert phone1.price == 100000
    assert phone1.quantity == 7
    assert phone1.number_of_sim == 1


def test_phone_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 13', 100000, 7, 1)"


def test_phone_add(phone1):
    item2 = Item('Клавиатура', 10000, 5)
    assert phone1 + item2 == 12
