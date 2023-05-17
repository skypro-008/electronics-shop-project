import pytest
from src.phone import Phone


@pytest.fixture
def xiaomi():
    return Phone("xiaomi", 68_000, 20, 2)


@pytest.fixture
def iphone():
    return Phone("IPhone 14 Pro", 100_000, 10, 1)


def test___str__(xiaomi):
    assert str(xiaomi) == 'xiaomi'


def test___repr__(iphone):
    assert repr(iphone) == "Phone('IPhone 14 Pro', 100000, 10, 1)"


def test_getter_number_of_sim(xiaomi):
    assert xiaomi.number_of_sim == 2


def test_setter_number_of_sim(iphone):
    iphone.number_of_sim = 5
    with pytest.raises(ValueError):
        iphone.number_of_sim = 0


def test_add_phone(iphone, xiaomi):
    assert iphone + xiaomi == 30


def test_err_add_phone(xiaomi):
    with pytest.raises(TypeError):
        xiaomi + int(10)
