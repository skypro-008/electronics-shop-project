"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


test_item = Item('Test', price=100, quantity=5)

def test_init():
    assert list(vars(test_item).values()) == ['Test', 100, 5]

def test_calculate_total_price():
    assert test_item.calculate_total_price() == 500

def test_apply_discount():
    Item.pay_rate = 0.9
    test_item.apply_discount()
    assert test_item.price == 90

def test_string_to_number():
    assert Item.string_to_number('10') == 10
    assert Item.string_to_number('10.0') == 10
    assert Item.string_to_number('10.9') == 10
    assert Item.string_to_number('-10.4') == -10

def test_string_to_digit_with_wrong_type():
    with pytest.raises(TypeError):
        Item.string_to_number(10)
    pytest.xfail("Ожидается сбой при передачи не строчного типа")

def test_instantiate_from_csv():
    items = Item.instantiate_from_csv()
    assert items[0].name == 'Смартфон'
    assert items[0].price == 100
    assert items[0].quantity == 1

