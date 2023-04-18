import pytest

from src.phone import Phone


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_init1():
    """Тестирует метод Item.__init__ с некорректным количеством SIM карт"""
    with pytest.raises(ValueError):
        Phone("phone", 1000, 10, "asd")
    with pytest.raises(ValueError):
        Phone("phone", 1000, 10, 0)


def test_repr(phone1):
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_setter1(phone1):
    phone1.number_of_sim = 4
    assert phone1.number_of_sim == 4


def test_setter2(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
