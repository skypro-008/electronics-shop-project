import pytest
from src.item import Item

@pytest.fixture
def example():
    return(Item("Смартфон", 10000, 20))


def test_calculate_total_price(example):
    assert example.calculate_total_price() == 200000


def test_apply_discount(example):
    example.pay_rate = 0.5
    example.apply_discount()
    assert example.price == 5000.0



