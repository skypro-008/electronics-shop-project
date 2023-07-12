import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def test_case_item1():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def test_case_item2():
    return Item("Ноутбук", 20000, 5)


@pytest.fixture
def test_case_phone1():
    return Phone("iPhone 14", 120000, 5, 2)


@pytest.fixture
def test_case_phone2():
    return Phone("iPhone 13", 110000, 2, 1)
