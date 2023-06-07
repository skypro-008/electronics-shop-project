from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)
phone2 = Phone("iPhone 5 SE", 10000, 3, 6)


def test_repr():
    assert phone1.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone2.__repr__() == "Phone('iPhone 5 SE', 10000, 3, 6)"

def test_str():
    assert phone1.__str__() == 'iPhone 14'
    assert phone2.__str__() == 'iPhone 5 SE'

def test_number_of_sim():
    assert phone1.number_of_sim == 2
    assert phone2.number_of_sim == 6