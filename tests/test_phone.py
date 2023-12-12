import pytest

from src.phone import Phone


@pytest.fixture
def item():
    return Phone("iPhone 14", 120_000, 5, 2)


def test__init__(item):
    assert item.__dict__ == {"_Item__name": "iPhone 14", "price": 120000, "quantity": 5, "_number_of_sim": 2}


def test__repr__(item):
    assert repr(item) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim_setter(item):
    item.number_of_sim = 2
    assert item.number_of_sim == 2


def test_raises_number_of_sim(item):
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        item.number_of_sim = 0
