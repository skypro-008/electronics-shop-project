from src.phone import Phone
import pytest


@pytest.fixture
def test_phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_init_phone(test_phone1):
    assert test_phone1.name == "iPhone 14"
    assert test_phone1.price == 120_000
    assert test_phone1.quantity == 5
    assert test_phone1.number_of_sim == 2


def test_number_of_sim(test_phone1):
    with pytest.raises(ValueError):
        test_phone1.number_of_sim = 0
        test_phone1.number_of_sim = -1
        test_phone1.number_of_sim = 1.5









