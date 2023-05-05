import pytest
from src.phone import Phone
from src.item import Item


def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_number_of_sim():
    """
    Тест для декоратора Property и сеттера, который не должен пропускать нулевое значение поддерживаемых сми-карт
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone1.number_of_sim = 1
    assert phone1.number_of_sim == 1
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_add():
    """
    Тест для add функции на сложение экземпляров класса Phone и Item по общему количеству товара в магазине
    """
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    item1 = Item("Смартфон", 10000, 20)
    assert item1 + phone1 == 25
    assert phone1 + phone1 == 10
    with pytest.raises(Exception):
        assert item1 + 1
    with pytest.raises(Exception):
        assert phone1 + 1
