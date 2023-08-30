from src.item import Item

item1 = Item("Samsung Galaxy", 60000, 10)


def test_init():
    assert item1.name == "Samsung Galaxy"
    assert item1.price == 60000
    assert item1.quantity == 10


def test_calculate_total_price():
    assert item1.calculate_total_price() == 600000


def test_apply_discount():
    assert item1.apply_discount() == 60000
