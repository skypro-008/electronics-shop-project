from src.phone import Phone
import pytest
data = Phone("Смартфон", 10000, 20, 2)
data1 = Phone("Смартфон", 10000, 20, 0)


def test_number_of_sim():

    assert data.number_of_sim == 2


def test_number_of_sim_0():
    """
    Тест на количество симм не равное 0
    """
    data.number_of_sim = 2
    with pytest.raises(ValueError):
        data1.number_of_sim = 0


def test_repr():
    """
    Тест магического метода __repr__
    """
    assert repr(data) == "Phone('Смартфон', 10000, 20, 2)"


def test_str():
    """
    Тест магического метода  __str__.
    """
    assert str(data) == 'Смартфон'
