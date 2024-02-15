from src.phone import Phone
import pytest


@pytest.fixture()
def phone_test():
    return Phone("Смартфон", 10000, 20, 2)


def test_number_of_sims_must_be_positive(phone_test):
    with pytest.raises(ValueError):
        phone_test.number_of_sim = 0


def test_number_of_sim(phone_test):
    phone_test.number_of_sim = 2


def test_repr(phone_test):
    """
    Тест магического метода __repr__
    """
    assert repr(phone_test) == "Phone('Смартфон', 10000, 20, 2)"


def test_str(phone_test):
    """
    Тест магического метода  __str__.
    """
    assert str(phone_test) == 'Смартфон'
