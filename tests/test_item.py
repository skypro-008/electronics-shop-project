"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest

@pytest.fixture
def exmp():
    return Item("Смарфтон", 10000, 20)

def calc(exmp):
    assert exmp.calculate_total_price() == 10000

def test_apply_discount(exmp):
    exmp.pay_rate = 0.8
    exmp.apply_discount()
    assert exmp.price == 8000

def test_name_setter(item):
    item.name="Телефон"
    assert item.name == "Телефон"
    item.name = "Супертелефон"
    assert item.name == "Супертелефон"

def test_instantiate_from_csv(item):
    item.instantiate_from_csv(5)
    assert len(item.all) == 5
    assert item.all[0].name == "Смарфтон"

def test_string_to_nember(item):
    assert isinstance(item.string_to_number(item.quantity), int)
