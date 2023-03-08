"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
from pytest import fixture


@fixture
def item1(): # Экземпляр товара "монитор"
    return Item('monitor', 15000, 7)


def test_init(item1):  # проверка правильности создания полей экземпляра
    assert item1.name == 'monitor'
    assert item1.price == 15000
    assert item1.quantity == 7


def test_calculate_total_price(item1):  # проверка метода подсчета общей стоимости товара
    assert item1.calculate_total_price() == item1.price * item1.quantity


def test_apply_discount(item1):  # проверка метода применения скидки
    old_price = item1.price  # цена до скидки
    item1.apply_discount()  # применяем скидку
    assert item1.price == old_price * item1.pay_rate  # проверяем, как сработало
