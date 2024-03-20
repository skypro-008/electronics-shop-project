import pytest

from src.item import Item
# Проверяем, что атрибуты класса Item были установлены правильно
@pytest.fixture
def item():
    return Item("Название товара", 1000, 5)

def test_init(item):
    assert item.name == "Название товара"
    assert item.price == 1000
    assert item.quantity == 5


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 5000


def test_discaunt_price(item):
    item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 500




