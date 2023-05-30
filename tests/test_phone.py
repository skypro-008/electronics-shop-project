import pytest

from src.item import Item
from src.phone import Phone

@pytest.fixture
def get_object():
    phone = Phone("Siemens A50", 1000, 30, 1)
    return phone


def test_repr_and_str(get_object):
    assert repr(get_object) == "Phone('Siemens A50', 1000, 30, 1)"
    assert str(get_object) == 'Siemens A50'

    with pytest.raises(TypeError):
        phone_2 = Phone("Siemens A50", 1000, 30, '1')

def test_number_fo_sim(get_object):
    assert get_object.number_of_sim == 1

    get_object.number_of_sim = 3
    assert get_object.number_of_sim == 3

    with pytest.raises(ValueError):
        get_object.number_of_sim = 0
        get_object.number_of_sim = -1
        get_object.number_of_sim = '1'

