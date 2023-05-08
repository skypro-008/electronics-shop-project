"""Здесь надо написать тесты с использованием pytest для модуля item."""
# from src.item import calculate_total_price
import pytest

from src.item import Item
from src.phone import Phone, KeyBoard


def test_name():
    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'
    with pytest.raises(Exception, match='Длина наименования товара превышает 10 символов.'):
        item.name = 'СуперСмартфон'


def test_name_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone1.name = 'iPhone 14'
    assert phone1.number_of_sim == 2


def test_name_keyboard():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert str(kb.language) == "EN"


def test_repr():
    item1 = Item('Телефон', 10000, 20)
    assert repr(item1) == "Item('Телефон', 10000, 20)"


def test_repr_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str():
    item1 = Item('Телефон', 10000, 20)
    assert str(item1) == "Телефон"


def test_str_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_change_lang():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    kb.change_lang()
    assert str(kb.language) == "RU"


def test_change_lang_one():
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    kb.change_lang().change_lang()
    assert str(kb.language) == 'EN'


def test_calculate_total_price():
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert 10000 * Item.pay_rate == 8000.0


def test_add_phone():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10


def test_string_to_number():
    """Статический метод, возвращающий число из числа-строки"""
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)


def test_item1_calculate_total_price(item1):
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert item1.calculate_total_price() == 'Общая стоимость Смартфон в магазине составляет: 200000'


def test_item1_apply_discount(item1):
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert item1.apply_discount() == 'Цена с учетом скидки 19% составляет 8000.0'


@pytest.fixture
def item2():
    return Item("Ноутбук", 20000, 5)


def test_item2_calculate_total_price(item2):
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert item2.calculate_total_price() == 'Общая стоимость Ноутбук в магазине составляет: 100000'


def test1_item2_apply_discount(item2):
    """Когда мы создаем экземпляр класса со значением item1, то calculate_total_price вернет нам результат"""
    assert item2.apply_discount() == 'Цена с учетом скидки 19% составляет 16000.0'


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert phone1.number_of_sim == 2
    with pytest.raises(ValueError, match='Количество физических SIM-карт должно быть целым числом больше нуля'):
        phone1.number_of_sim = 0
