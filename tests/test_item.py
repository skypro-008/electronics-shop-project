import pytest

from src.item import Item, InstantiateCSVError
from src.phone import Phone


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


def test_repr():
    """
    Тестирует метод repr
    """
    item1 = Item("Ноутбук", 100000, 4)
    assert repr(item1) == "Item('Ноутбук', 100000, 4)"


def test_str():
    """
    Тестирует метод str
    """
    item1 = Item("Ноутбук", 100000, 4)
    assert str(item1) == 'Ноутбук'


def test_add(test_class):
    """
    Тестируем метод add
    """
    item1 = test_class
    phone1 = Phone("Iphone 13", 120000, 22, 2)

    assert item1 + phone1 == 24
    assert phone1 + phone1 == 44


def test_instantiate_from_csv_not_found():
    """
    Тестирует метод instantiate_from_csv если файл отсутствует
    """
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()


def test_instantiate_from_csv_error():
    """
    Тестирует метод instantiate_from_csv если файл поврежден (отсутствует одна из колонок данных)
    """

    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
