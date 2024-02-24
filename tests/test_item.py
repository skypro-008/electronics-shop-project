from src.item import Item

date = Item("Смартфон", 10000, 20)


def test_calculate_total_price():
    """Тест проверки выплнения метода total price"""
    assert date.calculate_total_price() == 200000
    assert date.quantity == 20


def test_apply_discount():
    """Тест проверки выплнения метода установочной скидки для конкретного товара"""
    date.pay_rate = 0.8
    date.apply_discount()
    assert date.price == 8000.0





"""Здесь надо написать тесты с использованием pytest для модуля item."""
