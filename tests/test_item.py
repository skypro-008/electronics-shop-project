"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item


def test_init_item(test_case_item1):
    """Тестирует инициализацию"""
    assert test_case_item1.name == "Смартфон"
    assert test_case_item1.price == 10000
    assert test_case_item1.quantity == 20
    assert len(test_case_item1.all) == 1
    assert type(test_case_item1.all[0]) == Item


def test_calculate_total_price(test_case_item1, test_case_item2):
    """Тестирует вычисление общей стоимости"""
    assert test_case_item1.calculate_total_price() == 200000
    assert test_case_item2.calculate_total_price() == 100000


def test_apply_discount(test_case_item1, test_case_item2):
    """Тестирует применение скидки"""
    Item.pay_rate = 0.8
    test_case_item1.apply_discount()

    assert test_case_item1.price == 8000.0
    assert test_case_item2.price == 20000


def test_getter(test_case_item1):
    """Тест геттера"""
    assert test_case_item1.name == "Смартфон"


def test_setter(test_case_item1):
    """Тест сеттера"""
    test_case_item1.name = 'Супер'
    assert test_case_item1.name == 'Супер'

    test_case_item1.name = 'СуперСмартфон'
    assert test_case_item1.name == 'СуперСмарт'


def test_instantiate_from_csv():
    """Тест чтения"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 5

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert item1.price == 100 and (type(item1.price) == float or type(item1.price) == int)
    assert item1.quantity == 1 and type(item1.quantity) == int


def test_string_to_number():
    """Тест перевода из строки в число"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
