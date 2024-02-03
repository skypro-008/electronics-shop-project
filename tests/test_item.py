from src.item import Item, InstantiateCSVError
import pytest

obj1 = Item("Смартфон", 10000, 20)
obj2 = Item("Ноутбук", 20000, 5)

def test_Item_init():
    """
    Тест создания экземпляра класса item.

    :param name: Название товара.
    :param price: Цена за единицу товара.
    :param quantity: Количество товара в магазине.
     """
    assert obj1.name == "Смартфон"
    assert obj1.price == 10000
    assert obj1.quantity == 20
    assert obj2.name == "Ноутбук"
    assert obj2.price == 20000
    assert obj2.quantity == 5

def test_calculate_total_price():
    """
    Тест рассчета общей стоимости конкретного товара в магазине.

    """
    obj1.calculate_total_price()
    obj2.calculate_total_price()
    assert obj1.total_price == 200000
    assert obj2.total_price == 100000

def test_apply_discount():
    """
    Тест применения установленной скидку для конкретного товара.
    """
    obj1.pay_rate = 0.8
    obj1.apply_discount()
    obj2.apply_discount()
    assert obj1.price == 8000
    assert obj2.price == 20000

def test_instantiate_from_csv():
    """
    Тест применения Класса-метода, инициализирующего экземпляры класса Item
    """
    obj3 = Item.all[1]
    assert obj3.name == "Ноутбук"
    Item.instantiate_from_csv('src/items.csv')
    assert len(Item.all) == 5
def test_string_to_number():
    """
    Тест применения статического метода перевода числа из строкового значения в числовое
    """
    assert Item.string_to_number("3.3") == 3
    assert Item.string_to_number("3.0") == 3

def test_name():
    """
    Тест длины имени товара
    """
    obj1.name = 'СуперСмартфон'
    assert obj1.name =='СуперСмарт'
    obj1.name = 'ноутбук'
    assert obj1.name == 'ноутбук'

def test__repr__():
    """
    Тест магического метода __repr__
    """
    assert repr(obj2) == "Item('Ноутбук', 20000, 5)"

def test__str__():
    """
    Тест магического метода __str__
    """
    assert str(obj2) == "Ноутбук"

def test__add__():
    """
    Тест магического метода __add__ сложение и проверка принадлежность к классу
    """
    assert obj1 + obj2 ==25

def test_FileNotFoundError():
    """
    Тест исключения FileNotFoundError
    """
    with pytest.raises(FileNotFoundError):
        a = 'test.csv'
        Item.instantiate_from_csv(a)

def test_InstantiateCSVError():
    """
    Тест исключения InstantiateCSVError
    """
    with pytest.raises(InstantiateCSVError):
        a = '../src/items.csv'
        Item.instantiate_from_csv(a)
#############################################