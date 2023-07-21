from src.phone import Phone


def test_repr():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert repr(phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_number_of_sim():
    phone = Phone("iPhone 14", 120_000, 5, 2)
    assert phone.number_of_sim == 2
    phone.number_of_sim = 0
    assert phone.number_of_sim == ValueError
