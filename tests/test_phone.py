from src.phone import Phone
import pytest
from test_item import product


@pytest.fixture()
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_magic(phone1):
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_summ(phone1, product):
    assert product + phone1 == 25
    assert phone1 + phone1 == 10
