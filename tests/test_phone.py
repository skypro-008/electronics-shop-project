from src.phone  import Phone
from src.item import Item


# TestCase для проверки добавления нового атрибута: количество сим карт
phone1 = Phone('Nokia', 25000, 6, 2)

def test_phone_sim():
    assert phone1.number_of_sim == 2

#TestCase для проверки сложения количества двух экземпляров
item1 = Item('LG', 15000, 6)
def test_add_objects():
    assert phone1 + item1 == 12



