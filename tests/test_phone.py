from src.phone import Phone
from src.item import Item
import pytest


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_phone_inherits_from_item(phone):
    assert isinstance(phone, Item)


def test_phone_str_representation(phone):
    assert str(phone) == "iPhone 14"


def test_phone_repr_representation(phone):
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_phone_addition(phone):
    other_phone = Phone("Samsung Note", 100_000, 3, 1)
    result = phone + other_phone
    assert result == 8


def test_phone_addition_with_item_raises_error(phone):
    item = Item("Laptop", 80000, 2)
    with pytest.raises(TypeError,
                       match="Неподдерживаемая операция"):
        result = phone + item


def test_phone_number_of_sim_property(phone):
    assert phone.number_of_sim == 2


def test_phone_set_invalid_number_of_sim_raises_error(phone):
    with pytest.raises(ValueError, match="Количество  SIM-карт должно быть целым числом"):
        phone.number_of_sim = -1
