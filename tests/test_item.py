"""Здесь надо написать тесты с использованием pytest для модуля item."""
import src.item as my_item
import pytest

def test_class_item():
    temp_item = my_item.Item('Смартфон',100,1)
    assert temp_item.name == 'Смартфон'
    assert int((1-temp_item.pay_rate)*100) == 15
    assert temp_item.__str__() == "Смартфон в количестве 1 шт по цене 100 руб."
    assert temp_item.__repr__() == "Item('Смартфон', 100, 1)"
    assert temp_item.calculate_total_price() == 100
    temp_item.apply_discount()
    assert temp_item.calculate_total_price() == 85


def test_nice_number_output():
    assert my_item.nice_number_output(10000000) == '10 000 000'
    assert my_item.nice_number_output(10000000.0111) == '10 000 000.0111'
