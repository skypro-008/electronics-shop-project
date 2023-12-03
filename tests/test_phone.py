import pytest
from random import randint, random
from src.phone import Phone


@pytest.mark.parametrize('name', [
    ("Ноутбук"),
    ("Смартфон")
])
def test_name_title(name):
    item = Phone(name, randint(10000, 100000), randint(1, 100), randint(1, 10))
    assert item.name.istitle() == True

def test_repr_output():
    item = Phone("Mac", randint(10000, 100000), randint(1, 100), randint(1, 10))
    assert repr(item) == f"Phone('{item.name}', {item.price}, {item.quantity}, {item.number_of_sim})"

