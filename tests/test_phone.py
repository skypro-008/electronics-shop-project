import pytest
import csv

from src.item import Item
from src.phone import Phone


@pytest.fixture
def phone1():
    phone1 = Phone("Смартфон", 10000, 20, 2)
    return phone1


@pytest.fixture
def phone2():
    phone2 = Phone("iPhone 14", 120000, 5, 1)
    return phone2


@pytest.fixture
def num_zero():
    return 0


def test__init__(phone1):
    assert phone1.number_of_sim == 2
    assert len(Phone.all_phone) == 1
    assert Phone.all_phone[0] == phone1


def test__repr__(phone1):
    assert repr(phone1) == "Phone('Смартфон', 10000, 20, 2)"


def test__str__(phone1):
    assert str(phone1) == 'Смартфон'


def test_num_sim_property(phone2):
    assert phone2.number_of_sim == 1


@pytest.mark.parametrize('num, expected', [
    (2, 2),
    (3, 3),
    (0, 'Количество физических SIM-карт должно быть целым числом больше нуля.'),
    (-1, 'Количество физических SIM-карт должно быть целым числом больше нуля.'),
    (10.5, 'Количество физических SIM-карт должно быть целым числом больше нуля.'),
    ('15', 'Количество физических SIM-карт должно быть целым числом больше нуля.'),
])
def test_num_sim(num, expected):
    """Проверяет выполнение фуекции num_sim() при допустимых значениях и вывод сообщения при недопустимых значениях"""
    if isinstance(num, int) and num > 0:
        phone2.number_of_sim = num
        assert phone2.number_of_sim == expected
    else:
        assert 'Количество физических SIM-карт должно быть целым числом больше нуля.' == expected
