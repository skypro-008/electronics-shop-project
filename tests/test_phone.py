from src.phone import Phone
from src.item import Item
import pytest


def test_phone_number_of_sim():
    phone = Phone("iPhone", 1000, 5, 2)
    assert phone.number_of_sim == 2

    phone.number_of_sim = 1
    assert phone.number_of_sim == 1

    with pytest.raises(ValueError):
        phone.number_of_sim = -1

    def test_inherited_class():
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        assert str(phone1) == 'iPhone 14'
        assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
        assert phone1.number_of_sim == 2

    def test_addition_with_parent_class():
        item1 = Item("Смартфон", 10000, 20)
        phone1 = Phone("iPhone 14", 120_000, 5, 2)
        result1 = item1 + phone1
        assert result1 == 25
        result2 = phone1 + phone1
        assert result2 == 10