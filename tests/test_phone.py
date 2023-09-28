from src.phone import Phone
import pytest


@pytest.fixture()
def test_phone():
    return Phone(name="iPhone 14", price=1000, quantity=10, number_of_sim=15)


def test_repr(test_phone):
    assert repr(test_phone) == "Phone('iPhone 14', 1000, 10, 15)"


def test_number_of_sim(test_phone):
    assert type(test_phone.number_of_sim) == int
    assert test_phone.number_of_sim == 15
    test_phone.number_of_sim = 2
    assert test_phone.number_of_sim == 2


def test_error_number_of_sim_value(test_phone):
    with pytest.raises(ValueError):
        test_phone.number_of_sim = 0
        test_phone.number_of_sim = -2


def test_init():
    with pytest.raises(TypeError):
        Phone(name="iPhone 14", price=1000, quantity=10, number_of_sim="string")

