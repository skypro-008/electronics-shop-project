"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def get_test_item():
    return Item("Телевизор", 12500, 220)


def test_legal_item(get_test_item):
    """Когда мы создаем экземпляр класса и проверяем корректность присвоения значениям полей экземпляра класса:
    - name: Название товара
    - price: Цена за единицу товара
    - quantity: Количество товара в магазине
    """
    assert get_test_item.name == "Телевизор"
    assert get_test_item.price == 12500
    assert get_test_item.quantity == 220


def test_legal_item_calc_methods(get_test_item):
    """Когда мы создаем экземпляр класса и проверяем корректность методов экземпляра класса:
    - calculate_total_price(): расчет общей стоимости конкретного товара в магазине
    - apply_discount(): применение установленной скидки для конкретного товара
    """
    assert get_test_item.calculate_total_price() == 2_750_000
    Item.pay_rate = 0.75
    get_test_item.apply_discount()
    assert get_test_item.price == 9375


def test_item_price_not_positive():
    """Когда мы создаем экземпляр класса с отрицательным значением цены за единицу товара, вернется ошибка."""
    with pytest.raises(ValueError):
        Item("Телевизор", -10000, 220)


def test_item_quantity_not_positive():
    """Когда мы создаем экземпляр класса с отрицательным значением количества товара, вернется ошибка."""
    with pytest.raises(ValueError):
        Item("Телевизор", 10000, -220)


def test_item_quantity_not_int():
    """Когда мы создаем экземпляр класса с нечисловым значением количества товара, вернется ошибка."""
    with pytest.raises(ValueError):
        Item("Телевизор", 10000, 'test_quantity')


def test_item_price_not_float():
    """Когда мы создаем экземпляр класса с нечисловым значением цены за единицу товара, вернется ошибка."""
    with pytest.raises(ValueError):
        Item("Телевизор", '20000', 220)


def test_string_to_number():
    """Тестируем статический метод, возвращающий число из числа-строки."""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test_name_getter(get_test_item):
    """Тестируем работу сеттера name"""
    # Отрезаем первые 10 символов названия товарной позиции
    get_test_item.name = 'СуперСмартфон'
    assert get_test_item.name == 'СуперСмарт'


def test_instantiate_from_csv():
    """Тестируем инициализацию списка элементов класса Item из файла src/items.csv"""
    Item.instantiate_from_csv()
    # Общее количество элементов в загруженном списке
    assert len(Item.all) == 5
    # Проверяем корректность загрузки первого элемента
    item_test = Item.all[0]
    assert item_test.name == 'Смартфон'
    # Проверяем корректность загрузки четвертого элемента
    item_test = Item.all[3]
    assert item_test.name == 'Мышка'
    assert item_test.price == 50
