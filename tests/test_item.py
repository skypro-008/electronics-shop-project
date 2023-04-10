import pytest

from src.item import Item


@pytest.fixture
def return_date():
    """Описание фикстуры для тестов"""
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(return_date):
    """Тест для функции подсчета полной суммы запасов товара"""
    assert return_date.calculate_total_price() == 200000


def test_apply_discount(return_date):
    """Тест для функции расчета цены со скидкой"""
    return_date.pay_rate = 0.8
    return_date.apply_discount()
    assert return_date.price == 8000


def test_string_to_number():
    """тест для статической функции класса"""
    assert Item.string_to_number("6.67") == 6


def test_init(return_date):
    """Тест для init, просто интересно было, смысла в нем нет"""
    assert return_date.price == 10000
    assert return_date.name == 'Смартфон'
    assert return_date.quantity == 20

def test_name():
    """тест для декоратора name, в случае длинного значения, более 10 символов,Значение не вносится! """
    item = Item("Утюг", 5, 10)
    item.name = "Чайник"
    assert item.name == "Чайник"
    item1 = Item("Утюг", 5, 10)
    item1.name = "Очень длинное слово которе не должно быть принято "
    assert item1.name == "Утюг"


def test_instantiate_from_csv():
    """Тест для класса - метода открытия файла csv"""
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert item1.price == 100
    assert item1.quantity == 1

    item2 = Item.all[1]
    assert item2.name == 'Ноутбук'
    assert item2.price == 1000
    assert item2.quantity == 3

def test_str(return_date):
    """тест для метода str"""
    assert str(return_date) == 'Смартфон'

def test_repr(return_date):
    assert repr(return_date) == "Item('Смартфон', 10000, 20)"
