import pytest
from src.phone import Phone
from src.item import Item

@pytest.fixture
def phone1():
    return Phone('HUAWEI P60', 60_000, 10, 2)

@pytest.fixture
def phone2():
    return Phone('Xiaomi 12T', 42_000, 15, 2)

@pytest.fixture
def item1():
    return Item("Смартфон", 10_000, 20)


def test_init(phone1):
    assert issubclass(Phone, Item)

    assert phone1.name == 'HUAWEI P60'
    assert phone1.price == 60_000
    assert phone1.quantity == 10
    assert phone1.number_of_sim == 2

    with pytest.raises(ValueError):
        phone1.number_of_sim = '5'

    with pytest.raises(ValueError):
        phone1.number_of_sim = 0

    phone1.number_of_sim = 5
    assert phone1.number_of_sim == 5


def test_repr(phone1):
    assert repr(phone1) == "Phone('HUAWEI P60', 60000, 10, 2)"


def test_add(phone1, phone2, item1):
    assert phone1 + phone2 == 25
    assert phone1 + item1 == 30
    assert item1 + phone2 == 35
    with pytest.raises(TypeError):
        phone1 + 10
