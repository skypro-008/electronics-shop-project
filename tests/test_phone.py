from src.phone import Phone
import pytest

def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert Phone.__repr__(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert Phone.__str__(phone1) == 'iPhone 14'