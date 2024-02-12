import pytest
from src.phone import Phone

@pytest.fixture
def phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1

def test__init(phone):
    assert phone.name == "iPhone 14"
    assert phone.price == 120_000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test_repr(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone):
    assert str(phone) == 'iPhone 14'

