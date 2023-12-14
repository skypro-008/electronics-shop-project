from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)


def test__str__():
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
