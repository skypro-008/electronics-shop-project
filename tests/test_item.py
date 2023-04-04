import pytest

from src.item import Item


@pytest.fixture
def return_date():
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(return_date):
    """Тест для функции подсчета полной суммы запасов товара"""
    assert return_date.calculate_total_price() == 200000


def test_apply_discount(return_date):
    """Тест для функции расчета цены со скидкой"""
    return_date.pay_rate = 0.8
    return_date.apply_discount()
    assert return_date.price == 8000


def test_init(return_date):
    """Тест для init, просто интересно было, смысла в нем нет"""
    assert return_date.price == 10000
    assert return_date.name == 'Смартфон'
    assert return_date.quantity == 20
