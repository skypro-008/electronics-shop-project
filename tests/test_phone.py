from src.phone import Phone
from src.item import Item

class RandomClass:
    pass

def test_init():
    p = Phone("name", 1, 2, 3)
    assert p.name == "name"
    assert p.price == 1
    assert p.quantity == 2
    assert p.number_of_sim == 3

def test_add():
    r = RandomClass
    p = Phone("name", 1, 2, 3)
    i = Item("name", 1, 2)
    assert p+i == 4
    try:
        output = p+r
    except AssertionError:
        output = 0

    assert output == None

