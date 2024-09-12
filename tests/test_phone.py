import pytest

from src.phone import Phone


@pytest.fixture()
def test_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_number_of_sim(test_phone):
    assert test_phone.number_of_sim == 2


def test_str_and_repr(test_phone):
    assert str(test_phone) == 'iPhone 14'
    assert repr(test_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim_setter():
    phone1 = Phone("iPhone 14", 120_000, 5, 0)
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
