import pytest

from src.phone import Phone

phone1 = Phone("IPhone", 100000, 10, 2)


def test_init():
    assert str(phone1) == 'IPhone'
    assert repr(phone1) == "Phone(IPhone, 100000, 10, 2)"
    assert phone1.count_of_sim == 2
