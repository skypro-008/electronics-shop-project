from src.item import Item
import pytest


def test_calculate_total_price(item_smartphone_10000_20,
                               item_notebook_20000_5,
                               item_notebook_lenovo_0_0,
                               item_notebook_aser_minus_25000_minus_15):
    """Тест расчёта общей стоимости конкретного товара"""
    assert item_smartphone_10000_20.calculate_total_price() == 200000
    assert item_notebook_20000_5.calculate_total_price() == 100000
    assert item_notebook_lenovo_0_0.calculate_total_price() == 0
    assert item_notebook_aser_minus_25000_minus_15.calculate_total_price() == 'Проверьте товары. Цена или количество не должны быть отрицательными.'


def test_apply_discount(pay_rate_1,
                        item_smartphone_10000_20,
                        item_notebook_20000_5,
                        item_notebook_lenovo_0_0,
                        item_notebook_aser_minus_25000_minus_15):
    """Тест установки скидки для конкретного товара"""
    item_smartphone_10000_20.pay_rate = pay_rate_1
    item_notebook_20000_5.pay_rate = pay_rate_1
    item_notebook_lenovo_0_0.pay_rate = pay_rate_1
    assert item_smartphone_10000_20.apply_discount() == 8000
    assert item_notebook_20000_5.apply_discount() == 16000
    assert item_notebook_lenovo_0_0.apply_discount() == 'Проверьте значения скидки или цены. Одно из них равно нулю.'
    assert item_notebook_aser_minus_25000_minus_15.apply_discount() == 'Проверьте значения скидки или цены. Одно из них меньше нуля'


def test_repr(item_smartphone_10000_20, item_notebook_20000_5, item_notebook_lenovo_0_0):
    """
    Тест на правильность преобразования объекта Item в строку для вывода в отладке
    """
    assert item_smartphone_10000_20.__repr__() == "Item('Смартфон', 10000, 20)"
    assert item_notebook_20000_5.__repr__() == "Item('Ноутбук', 20000, 5)"
    assert item_notebook_lenovo_0_0.__repr__() == "Item('Ноутбук_lenovo', 0, 0)"


def test_str(item_smartphone_10000_20, item_notebook_20000_5, item_notebook_lenovo_0_0):
    """
    Тест на правильность преобразования объекта Item в строку
    для представления элемента класса пользователю
    """
    assert item_smartphone_10000_20.__str__() == 'Смартфон'
    assert item_notebook_20000_5.__str__() == 'Ноутбук'
    assert item_notebook_lenovo_0_0.__str__() == 'Ноутбук_lenovo'


def test_get_all_items(item_smartphone_10000_20, item_notebook_20000_5):
    """ Тестируем возвращаемость списка товаров"""
    Item.all = [item_smartphone_10000_20.__repr__(), item_notebook_20000_5.__repr__()]
    assert Item.all == ["Item('Смартфон', 10000, 20)",
                        "Item('Ноутбук', 20000, 5)"]


def test_get_count_items(test_all_items):
    """Тест подсчёта общего количества товаров"""
    Item.all = test_all_items
    assert Item.get_count_items() == 2


def test_get_name(item_notebook_lenovo_0_0):
    assert item_notebook_lenovo_0_0.name == 'Ноутбук_lenovo'


def test_set_name_valid(item_notebook_lenovo_0_0):
    item_notebook_lenovo_0_0.name = 'Lenovo'
    assert item_notebook_lenovo_0_0.name == 'Lenovo'


def test_set_name_invalid(item_notebook_lenovo_0_0):
    with pytest.raises(Exception) as exc_info:
        item_notebook_lenovo_0_0.name = '12345678901'
    assert str(exc_info.value) == 'Длина товара превышает 10 символов.'
    assert item_notebook_lenovo_0_0.name == 'Ноутбук_lenovo'


def test_instantiate_from_csv():
    """ Проверка создания объектов из файла """
    Item.instantiate_from_csv()  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам


def test_string_to_number(strings):
    """
    Проверка перевода строки в число
    """
    string_1, string_2, string_3 = strings.split(', ')

    assert Item.string_to_number(string_1) == 0
    assert Item.string_to_number(string_2) == 5
    assert Item.string_to_number(string_3) == 5
