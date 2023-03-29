import pytest
from src.phone import Phone
from src.item import Item


@pytest.fixture
def test_data_one():
    return "iPhone 14", 10000, 20, 2


@pytest.fixture
def test_data_two():
    return "Samsung s20+", 20000, 5, 0


def test_phone_py_one(test_data_one):
    class_exemplar = Phone(*test_data_one)
    assert class_exemplar.name == "iPhone 14"
    assert str(class_exemplar) == 'iPhone 14'
    assert repr(class_exemplar) == "Phone('iPhone 14', 10000, 20, 2)"
    assert class_exemplar.number_of_sim == 2

    item1 = Item("Смартфон", 10000, 20)
    assert item1 + class_exemplar == 40
    assert class_exemplar + class_exemplar == 40

    class_exemplar.number_of_sim = 3
    assert class_exemplar.number_of_sim == 3

    class_exemplar.number_of_sim = 0
    assert class_exemplar.number_of_sim == 3
