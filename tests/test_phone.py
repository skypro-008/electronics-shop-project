from src.phone import Phone




def test_phone_class():
    phone_1 = Phone(name="name1", price=10, quantity=2, simcard_count=2)
    assert phone_1.name == 'name1'
    assert phone_1.simcard_count == 2
    assert phone_1.quantity == 2

def test_add_phone():
    phone_2 = Phone(name="name2", price=5, quantity=5, simcard_count=3)
    phone_1 = Phone(name="name1", price=10, quantity=2, simcard_count=2)
    assert phone_1 + phone_2 ==7