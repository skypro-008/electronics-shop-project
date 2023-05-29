from src.phone import Phone
import pytest


@pytest.fixture
def phone_1():
    return Phone("Samsung", 34000, 8, 1)


@pytest.fixture
def phone_2():
    return Phone("Sony", 46000, 6, 2)


def test__repr__(phone_1, phone_2):
    assert repr(phone_1) == "Phone('Samsung', 34000, 8, 1)"
    assert repr(phone_2) == "Phone('Sony', 46000, 6, 2)"


def test_number_of_sim(phone_1):
    assert phone_1.number_of_sim == 1
    phone_1.number_of_sim = 2
    assert phone_1.number_of_sim == 2
    with pytest.raises(ValueError):
        phone_1.number_of_sim = 0
