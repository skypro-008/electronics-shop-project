
import pytest
from src.phone import Phone


@pytest.fixture
def phone_test():
    return Phone("Самсунг", 50000, 5, 2)


def test___repr__(phone_test):
    assert repr(phone_test) == "Phone('Самсунг', 50000, 5, 2)"


def test_number_of_sim(phone_test):
    assert phone_test.number_of_sim == 2


def test_number_of_sim(phone_test):
    phone_test.number_of_sim = 1
    assert phone_test.number_of_sim == 1