from src.phone import Phone


def test_add():
    phone1 = Phone('iPhone14', 120000, 10, 2)
    phone2 = Phone('iPhone15', 200000, 5, 2)
    assert phone1.quantity + phone2.quantity == 15


def test_repr():
    phone1 = Phone('iPhone14', 120000, 10, 2)
    assert repr(phone1) == "Phone('iPhone14', 120000, 10, 2)"
