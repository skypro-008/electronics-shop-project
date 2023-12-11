import pytest

from src.phone import Phone

phone1 = Phone("iPhone 10", 20000, 5, 2)


def test_item_init():
    assert phone1.name == 'iPhone 10'
    assert phone1.price == 20000
    assert phone1.quantity == 5
    assert phone1.number_of_sim == 2


def test_repr():
    assert repr(phone1) == "Phone('iPhone 10', 20000, 5, 2)"


def test_verify_sim():
    phone = Phone("iPhone 10", 20000, 5, 2)
    with pytest.raises(ValueError) as e:
        phone.number_of_sim = -1
    assert str(e.value) == 'Количество физических SIM-карт должно быть целым числом больше нуля.'


def test_number_of_sim():
    phone2 = Phone("iPhone12", 70000, 5, 1)
    phone2.number_of_sim = 1
