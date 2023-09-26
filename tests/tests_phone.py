from src.phone import Phone

phone = Phone('iphone', 10000, 5, 2)


def test_name():
    phone.name = 'iphone'
    assert phone.name == 'iphone'


def test_repr():
    assert repr(phone) == "Phone('iphone', 10000, 5, 2)"


def test_phone_sim_cards():
    assert phone.number_of_sim == 2


def test_phone_sim_cards_setter():
    phone.number_of_sim = 3
    assert phone.number_of_sim == 3
