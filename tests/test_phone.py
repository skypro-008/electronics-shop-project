from src.phone import Phone


def test_phone_class():
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_sim_cards == 2
    assert phone1.name == "iPhone 14"
    assert phone1.price == 120_000
    assert phone1.quantity == 5
