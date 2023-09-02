import pytest
from _pytest.python_api import raises

from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("Смартфон", 10000, 20, 2)


def test_init(phone):
    assert phone.number_of_sim == 2


def test_repr(phone):
    assert repr(phone) == "Phone('Смартфон', 10000, 20, 2)"


def test_positive_sim_cards_count(phone):
    err_msg = 'Количество физических SIM-карт должно быть больше нуля'
    with raises(ValueError, match=err_msg):
        phone.number_of_sim = 0