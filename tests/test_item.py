import pytest

from src.item import Item


# Создаем тестовый экземпляр товара для использования в тестах
@pytest.fixture
def test_item():
    return Item("Test Item", 10.0, 5)


def test_calculate_total_price(test_item):
    assert test_item.calculate_total_price() == 50.0


def test_apply_discount(test_item):
    test_item.apply_discount()
    assert test_item.price == 10.0 * Item.pay_rate
