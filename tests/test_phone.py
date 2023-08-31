import pytest
from src.phone import Phone


@pytest.fixture
def test_phone1():
    return Phone("Телефон1", 100, 2, 2)


def test_repr(test_phone1):
    assert test_phone1.__repr__() == "Phone('Телефон1', 100, 2, 2)"


def test_str(test_phone1):
    assert test_phone1.__str__() == 'Телефон1'


def test_number_of_sim(test_phone1):
    test_phone1.number_of_sim = 1
    assert test_phone1.number_of_sim == 1
