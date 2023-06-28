import pytest
from src.item import Item


@pytest.fixture
def one_item():
    return Item('Toster', 10_000, 10)


def test_repr(one_item):
    """
    тест инициализации товара по параметрам
    """
    assert one_item.__repr__() == ('Toster', 10_000, 10)

def test_calculate_total_price(one_item):
    """
    тест расчета общей стоимости товара
    """

    assert one_item.calculate_total_price() == 100_000

def test_apply_discount(one_item):
    """
    тест применения скидки к товару
    """

    assert one_item.apply_discount(10) == 90_000
    assert one_item.apply_discount(0) == 100_000
