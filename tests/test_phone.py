import pytest
from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_repr(phone):
    """
    Проверка магической функции repr
    """
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone):
    """
    Проверка магической функции str
    """
    assert str(phone) == "iPhone 14"
