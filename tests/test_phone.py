import pytest
import csv
import os
from src.phone import Phone

def test_phone_initialization():
    phone = Phone('Test Item', 100.0, 5, 1)
    assert phone.name == "Test Item"
    assert phone.price == 100.0
    assert phone.quantity == 5
    assert phone.number_of_sim == 1

def test_phone_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_check_number_of_sim():
    phone = Phone("Test Phone", 100.0, 5, 1)
    with pytest.raises(ValueError, match='Количество физических SIM-карт должно быть целым числом больше нуля.'):
        phone.check_number_of_sim(-1)