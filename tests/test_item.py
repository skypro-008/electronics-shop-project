"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


@pytest.fixture
def smartphone():
    """возвращает экземпляр класса Смартфон с ценой 10000 и кол-вом 20"""
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def notebook():
    """возвращает экземпляр класса Ноутбук с ценой 20000 и кол-вом 5"""

    return Item("Ноутбук", 20000, 5)


def test__item_all(smartphone, notebook):
    """тестируем атрибут хранения созданных экземпляров класса Item"""
    item1 = smartphone
    item2 = notebook
    assert Item.all == [item1, item2]


def test__calculate_total_price(smartphone, notebook):
    """тестируем метод вычисления суммы всех товаров отдельного экземпляра"""

    assert smartphone.calculate_total_price() == 200000
    assert notebook.calculate_total_price() == 100000


def test__apply_discount(smartphone, notebook):
    """тестируем метод применения скидки экземпляров класса с разным значением уровня цен"""

    # применяем скидку для экземпляра (класса Item) "ноутбук" (pay_rate = 1, скидка 0%)
    notebook.apply_discount()
    # устанавливаем новый уровень цен (скидка 20%)
    Item.pay_rate = 0.8
    # применяем скидку для экземпляра "смартфон"
    smartphone.apply_discount()

    assert smartphone.price == 8000.0
    assert notebook.price == 20000


def test__item_repr(smartphone, notebook):
    """тестурем метод repr для каждого экземпляра класса Item"""

    assert smartphone.__repr__() == f'Item({smartphone.name}, {smartphone.price}, {smartphone.quantity})'
    assert notebook.__repr__() == f'Item({notebook.name}, {notebook.price}, {notebook.quantity})'


def test__item_name(smartphone):
    """тестирем сеттер установки значения атрибуте name"""

    item1 = smartphone
    item1.name = 'Тестировщик'
    assert smartphone.name == 'Тестировщи'

    item1.name = 'Тест'
    assert smartphone.name == 'Тест'


def test__string_to_number():
    """тестируем метод конвертации строки в число"""

    assert Item.string_to_number("10.5") == 10
    with pytest.raises(ValueError):
        Item.string_to_number("abc")
    assert Item.string_to_number(10) == print('Данная запись не является числом-строкой')


def test__instantiate_from_csv():
    """тестируем создание экземпляров класса Item из item.csv и запись в Item.all"""

    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
