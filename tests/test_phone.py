from src.phone import Phone


def test_str():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'


def test_repr():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    phone2 = Phone("iPhone 15", 160_000, 7, 1)
    assert phone1.number_of_sim == 2
    assert phone2.number_of_sim == 1