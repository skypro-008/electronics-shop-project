from src.phone import Phone


def test_phone_number_of_sim_setter_valid_value():
    phone = Phone("Samsung Galaxy S21", 800, 10, 1)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2


def test_phone_number_of_sim_setter_invalid_value():
    phone = Phone("Samsung Galaxy S21", 800, 10, 1)
    try:
        phone.number_of_sim = -2
    except ValueError as e:
        assert str(e) == "Количество физических SIM-карт должно быть целым числом больше нуля."


def test_phone_number_of_sim_property():
    phone = Phone("Samsung Galaxy S21", 800, 10, 1)
    assert phone.number_of_sim == 1


def test_phone_representation():
    phone = Phone("Samsung Galaxy S21", 800, 10, 1)
    assert repr(phone) == "Phone('Samsung Galaxy S21', 800, 10, 1)"


def test_phone_str():
    phone = Phone("Samsung Galaxy S21", 800, 10, 1)
    assert str(phone) == "Samsung Galaxy S21"