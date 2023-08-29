import pytest

from src.phone import Phone


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
