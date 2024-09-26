import pytest
import coverage
from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def test_phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_name(test_phone1):
    assert str(test_phone1) == "iPhone 14"
    assert repr(test_phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert test_phone1.number_of_sim == 2


def test_add(test_item1, test_phone1):
    assert test_phone1 + test_item1 == 25