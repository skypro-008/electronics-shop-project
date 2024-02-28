import pytest
from tests.test_item import example
from config import root_csv
from src.phone import Phone

@pytest.fixture
def example_2():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    return phone1

def test_phone_class(example, example_2):
    assert str(example_2) == 'iPhone 14'
    assert repr(example_2) == "Phone('iPhone 14', 120000, 5, 2)"
    assert example_2.number_of_sim == 2
    assert example + example_2 == 25
    assert example_2 + example_2 == 10

    with pytest.raises(ValueError):
        example_2.number_of_sim = 0