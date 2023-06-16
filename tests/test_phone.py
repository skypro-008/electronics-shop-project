"""Здесь надо написать тесты с использованием pytest для модуля phone."""

import pytest
from src.phone import Phone
from src.item import Item

@pytest.fixture
def test_phone():
    return Phone("test_ph14", 135000, 4, 2)

@pytest.fixture
def test_item():
    return Item("test_PC", 35000, 4)


def test__init__(test_phone):
    assert test_phone.name == "test_ph14"
    assert test_phone.price == 135000
    assert test_phone.number_of_sim == 2
    test_phone.number_of_sim = 4
    assert test_phone.number_of_sim == 4

def test__str__(test_phone):
    assert str(test_phone) == "test_ph14"


def test__repr__(test_phone):
    assert repr(test_phone) == "Phone('test_ph14', 135000, 4, 2)"


def test__add__(test_phone, test_item):
    assert test_phone + test_item == 8
