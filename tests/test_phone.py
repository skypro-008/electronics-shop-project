import pytest

from src.phone import Phone


def test_number_of_sim():
    phone = Phone("",0,0,1)
    assert phone.number_of_sim == 1
    with pytest.raises(ValueError):
        phone.number_of_sim = '2'
    with pytest.raises(ValueError):
        phone.number_of_sim = 1.1
    with pytest.raises(ValueError):
        phone.number_of_sim = -2

