from src.phone import Phone
import pytest

from pytest import fixture

@fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)

def test_phone(phone):
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2