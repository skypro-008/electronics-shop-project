from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)

def test___repr__():
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"

def test___str__():
    assert str(phone1) == 'iPhone 14'


def test_number_of_sim():
    assert phone1.number_of_sim == 2




