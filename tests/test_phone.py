from src.phone import Phone

test = Phone("iPhone 13", 100000, 5, 2)


def test___str__():
    assert str(test) == 'iPhone 13'


def test___repr__():
    assert (repr(test)) == "Phone('iPhone 13', 100000, 5, 2)"
