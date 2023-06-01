import pytest

from src.phone import Phone
from src.item import Item


@pytest.fixture
def phone1():
    return Phone('Xiaomi 5000 GeForce GT Plasma 13T Ultra Pro Twin Turbo Plus Max Ultra Mini 1024Gb', 20000, 1, 2)


@pytest.fixture
def phone2():
    return Phone('iPhone 12', 5000, 10, 1)


def test_init(phone1):
    assert phone1.name == 'Xiaomi 5000 GeForce GT Plasma 13T Ultra Pro Twin Turbo Plus Max Ultra Mini 1024Gb'
    assert phone1.price == 20000
    assert phone1.number_of_sim == 2


def test_init__wrong_number_of_sim(phone2):
    with pytest.raises(ValueError):
        phone2.number_of_sim = 0

    with pytest.raises(ValueError):
        Phone('Brick', 1, 1, 'один')


def test_str(phone1):
    assert str(phone1) == 'Xiaomi 5000 GeForce GT Plasma 13T Ultra Pro Twin Turbo Plus Max Ultra Mini 1024Gb'


def test_repr(phone2):
    assert repr(phone2) == "Phone('iPhone 12', 5000, 10, 1)"


def test_add(phone1, phone2):
    assert phone1 + phone2 == 11