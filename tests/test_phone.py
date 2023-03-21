
import pytest
from src.phone import Phone

@pytest.fixture
def item_phone():
    return Phone("phone", 10000, 5, 2)

def test_phone_init1():
    """Тестирует метод Item.__init__ с некорректным количеством SIM карт"""
    with pytest.raises(ValueError):
        Phone("phone", 1000, 10, "asd")
    with pytest.raises(ValueError):
        Phone("phone", 1000, 10, 0)

def test_repr(item_phone):
    assert item_phone.__repr__() == "Phone('phone', 10000, 5, 2)"

def test_setter1(item_phone):
    item_phone.number_of_sim = 4
    assert item_phone.number_of_sim == 4

def test_setter2(item_phone):
    with pytest.raises(ValueError):
        item_phone.number_of_sim = 0