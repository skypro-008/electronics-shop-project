import pytest
import csv

from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone1():
    phone1 = Phone("Смартфон", 10000, 20, 2)
    return phone1


def test__init__(phone1):
    assert phone1.number_of_sim == 2
    assert len(Phone.all_phone) == 1


def test__repr__(phone1):
    assert repr(phone1) == "Phone('Смартфон', 10000, 20, 2)"


def test__str__(phone1):
    assert str(phone1) == 'Смартфон'
