from src.phone import Phone
import pytest


def test_init_phone(test_case_phone1):
    """Тестирует инициализацию"""
    assert test_case_phone1.name == "iPhone 14"
    assert test_case_phone1.price == 120_000
    assert test_case_phone1.quantity == 5
    assert test_case_phone1.number_of_sim == 2


def test_setter(test_case_phone1):
    """Тест сеттера"""
    with pytest.raises(ValueError):
        test_case_phone1.number_of_sim = 2.3

    with pytest.raises(ValueError):
        test_case_phone1.number_of_sim = 0

    test_case_phone1.number_of_sim = 10
    assert test_case_phone1.number_of_sim == 10


def test_repr_phone(test_case_phone1):
    """Тест магического метода repr"""
    assert repr(test_case_phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add_phone(test_case_phone1, test_case_phone2, test_case_item1):
    """Тест сложения"""
    assert test_case_item1 + test_case_phone1 == 25
    assert test_case_phone1 + test_case_item1 == 25
    assert test_case_phone1 + test_case_phone2 == 7
