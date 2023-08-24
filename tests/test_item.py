import pytest

from src import item
from src.item import Item


@pytest.fixture()
def test_class():

    return Item("Смартфон", 12000, 2)


def test_calculate_total_price(test_class):
    """
    Тестирует функцию подсчета общей стоимости конкретного товара
    """

    assert test_class.calculate_total_price() == 24000


def test_apply_discount(test_class):
    """
    Тестирует функцию применения скидки на определенный товар
    """
    test_class.apply_discount()
    assert test_class.price == test_class.price * Item.pay_rate


def test_name(test_class):
    """
    Тестирует сеттер на проверку количества символов в name
    """
    item1 = test_class
    assert item1.name == "Смартфон"
    item1.name = "СуперСмартфон"
    assert item1.name == "СуперСмарт"


def test_string_to_number():
    """
    Тестирует функцию перевода числа-строки в число
    """
    number_string_1 = "5.0"
    number_string_2 = "10"

    assert Item.string_to_number(number_string_1) == 5
    assert Item.string_to_number(number_string_2) == 10
