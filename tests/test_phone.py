import pytest

from src.phone import Phone
from src.item import Item


@pytest.fixture
def test_class():

    return Phone('Iphone 14', 100000, 3, 2)


def test_str(test_class):
    """
    Тестирует метод str
    """
    phone1 = test_class
    assert str(phone1) == 'Iphone 14'


def test_repr(test_class):
    """
    Тестируем метод repr
    """
    phone1 = test_class
    assert repr(phone1) == "Phone('Iphone 14', 100000, 3, 2)"


def test_add(test_class):
    """
    Тестируем метод add
    """
    item1 = Item("Смартфон", 10000, 20)
    phone1 = test_class

    assert item1 + phone1 == 23
    assert phone1 + phone1 == 6
