from src.phone import Phone

phone1 = Phone("iPhone 14", 120_000, 5, 2)
phone2 = Phone("iPhone 14", 120_000, 5, 0)


def test__str__():
    assert str(phone1) == 'iPhone 14'
    assert repr(phone1) == "Phone('iPhone 14', 120000, 5, 2)"
    assert phone1.number_of_sim == 2
    assert phone2.number_of_sim == 'Количество физических SIM-карт должно быть целым числом больше нуля.'
