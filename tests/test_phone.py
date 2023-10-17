from src.item import Item
from tests.test_item import item
from src.phone import Phone
import pytest


@pytest.fixture
def phone():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    return phone


def test___repr__(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test___str__(phone):
    assert str(phone) == 'iPhone 14'


def test__add__(item, phone):
    assert item + phone == 25


def test_number_of_sim(phone):
    with pytest.raises(ValueError):
        phone.number_of_sim = 0




