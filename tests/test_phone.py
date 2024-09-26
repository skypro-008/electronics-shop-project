import pytest
from src.phone import Phone


@pytest.fixture
def fix_phone_class():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_number_of_sim(fix_phone_class):
    """Тест аргумента кол-во сим-карт"""
    assert fix_phone_class.number_of_sim == 2
    fix_phone_class.number_of_sim = 4
    assert fix_phone_class.number_of_sim == 4
    with pytest.raises(ValueError):
        fix_phone_class.number_of_sim = 0
        assert fix_phone_class.number_of_sim == "Количество физических SIM-карт должно быть целым числом больше нуля."


def test_repr_str(fix_phone_class):
    """тест repr и str"""
    assert str(fix_phone_class) == 'iPhone 14'
    assert repr(fix_phone_class) == "Phone('iPhone 14', 120000, 5, 2)"
