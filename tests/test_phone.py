import pytest
from src.phone import Phone
from src.item import Item

def test_number_of_sim_valid_value():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3

def test_number_of_sim_negative_value():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    with pytest.raises(ValueError) as e:
        phone.number_of_sim = -1
    assert str(e.value) == "Количество физических SIM-карт должно быть целым числом больше или равно нулю."

def test_number_of_sim_non_integer_value():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    with pytest.raises(ValueError) as e:
        phone.number_of_sim = 2.5
    assert str(e.value) == "Количество физических SIM-карт должно быть целым числом больше или равно нулю."


def test_add_same_item_types():
    item1 = Item("Товар 1", 100, 5)
    item2 = Item("Товар 2", 200, 3)
    result = item1 + item2
    assert result == 8

def test_add_item_with_non_item_type():
    item = Item("Товар", 100, 5)
    with pytest.raises(Exception):
        item + "Некоторый другой объект"

def test_repr():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    expected_repr = "Phone('iPhone 14', 120000, 5, 2)"
    assert repr(phone) == expected_repr