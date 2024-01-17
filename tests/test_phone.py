from src.phone import Phone
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
phone1 = Phone("iPhone 1", 120_000, 2, 2)
phone2 = Phone("iPhone 2", 150_000, 5, 3)


def test_Phone_init():
    """
    Тест создания экземпляра класса Phone.
    :param name: Название товара.
    :param price: Цена за единицу товара.
    :param quantity: Количество товара в магазине.
    :param number_of_sim: Количество сим-карт.
     """
    assert phone1.name == "iPhone 1"
    assert phone1.price == 120_000
    assert phone1.quantity == 2
    assert phone1.number_of_sim == 2
    assert phone2.name == "iPhone 2"
    assert phone2.price == 150_000
    assert phone2.quantity == 5
    assert phone2.number_of_sim == 3


def test__repr__():
    """
    Тест магического метода __repr__
    """
    assert repr(phone1) == "Phone('iPhone 1', 120000, 2, 2)"
    assert repr(phone2) == "Phone('iPhone 2', 150000, 5, 3)"


def test__add__():
    """
    Тест магического метода __add__ сложение и проверка принадлежность к классу
    """
    assert item1 + phone1 == 22
    assert phone2 + phone1 == 7
    assert phone1 + 10000 == ValueError("Нельзя сложить классы 'Phone' или 'Item' с не 'Phone' или 'Item'")


def test_number_of_sim():
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
    phone1.number_of_sim = 0
    assert phone1.number_of_sim == ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
