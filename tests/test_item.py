import pytest
from src.item import Item


@pytest.fixture()
def test_class():

    return Item("Смартфон", 12000, 2)


def test_calculate_total_price(test_class):
    """
    Тестирует функцию подсчета общей стоимости конкретного товара
    """

    assert test_class.calculate_total_price() == 24000