from src.phone import Phone




def test_phone_class():
    phone_1 = Phone(name="name1", price=10, quantity=2, number_of_sim=21)
    assert phone_1.name == 'name1'
    assert phone_1.number_of_sim == 21
    assert phone_1.quantity == 2

def test_add_phone():
    phone_2 = Phone(name="name2", price=5, quantity=5, number_of_sim=2)
    phone_1 = Phone(name="name1", price=10, quantity=2, number_of_sim=3)
    assert phone_1 + phone_2 ==7