from src.phone import Phone

import pytest


@pytest.fixture
def item():
    item = Phone(name="Мерседес", price=45.97, quantity=40, sim=5)
    return item
def test_str(item):
    assert str(item) == "Мерседес"

def test_repr(item):
    assert repr(item) == "Phone('Мерседес', 45.97, 40, 5)"


def test_number_of_sim():
    with pytest.raises(ValueError) as t:
        phone = Phone('Iphone 12', 12000, 35, 0)
        assert str(t.value) == "Количество физических SIM-карт должно быть целым числом больше нуля."