import pytest
from src.phone import Phone


def test__repr__():
    """
    Тест для repr
    """
    phone2 = Phone('Samsung S20', 9000, 4, 2)
    assert repr(phone2) == "Phone('Samsung S20', 9000, 4, 2)"


def test__str__():
    """
    Тест для str
    """
    phone2 = Phone('Samsung S20', 9000, 4, 2)
    assert str(phone2) == "Samsung S20"


def test_number_of_sim_setter():
    """
    Тестируем сеттер
    """
    phone = Phone('Samsung S20', 10000.0, 5, 2)
    # Тестируем корректные значения
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1

    phone.number_of_sim = 2
    assert phone.number_of_sim == 2

    # Тестируем не корректные значения
    # try:
    #     phone.number_of_sim = 0
    #     assert False, "Exception not raised"
    # except Exception as e:
    #     assert str(e) == "Количество физических SIM-карт должно быть целым числом больше нуля."
    #
    # try:
    #     phone.number_of_sim = 3
    #     assert False, "Exception not raised"
    # except Exception as e:
    #     assert str(e) == "Количество физических SIM-карт должно быть целым числом больше нуля."
    with pytest.raises(Exception):
        phone.number_of_sim = -1

    with pytest.raises(Exception):
        phone.number_of_sim = 0

    with pytest.raises(Exception):
        phone.number_of_sim = 3
