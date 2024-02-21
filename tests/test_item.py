import pytest
from src.item import Item
from src.phone import Phone
from config import root_csv
from src.item import InstantiateCSVError

@pytest.fixture
def example():
    return(Item("Смартфон", 10000, 20))


def test_init(example):
    assert example.name == "Смартфон"
    assert example.price == 10000
    assert example.quantity == 20
    example.name = 'СуперСмартфон'
    assert example.name == 'СуперСмарт'

def test_calculate_total_price(example):
    assert example.calculate_total_price() == 200000


def test_apply_discount(example):
    example.pay_rate = 0.5
    example.apply_discount()
    assert example.price == 5000.0

def test_instantiate_from_csv():
    Item.instantiate_from_csv(root_csv)
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'

def test_instantiate_from_csv2():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv('')

def test_instantiate_from_csv3():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("../src/item.py")

def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5

def test_repr(example):
    assert repr(example) == "Item('Смартфон', 10000, 20)"

def test_str(example):
    assert str(example) == 'Смартфон'