import pytest


def test_repr(phone_samsung_16000_4_3, phone_iphone14_120000_5_2):
    """
    Тест на правильность преобразования объекта Phone в строку для вывода в отладке
    """
    assert phone_samsung_16000_4_3.__repr__() == "Phone('Samsung', 16000, 4, 3)"
    assert phone_iphone14_120000_5_2.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(phone_samsung_16000_4_3, phone_iphone14_120000_5_2):
    """
    Тест на правильность преобразования объекта Phone в строку
    для представления элемента класса пользователю
    """
    assert phone_samsung_16000_4_3.__str__() == 'Samsung'
    assert phone_iphone14_120000_5_2.__str__() == 'iPhone 14'


def test_add(item_notebook_20000_5, phone_iphone14_120000_5_2, phone_samsung_16000_4_3):
    """
    Тест на сложение экземпляров классов Phone и Item.
    """
    assert phone_iphone14_120000_5_2.__add__(item_notebook_20000_5) == 10
    assert phone_iphone14_120000_5_2.__add__(phone_samsung_16000_4_3) == 9


def test_fail_add(phone_samsung_16000_4_3):
    """
    Нельзя складывать экземпляры Phone и Item с экземплярами не Phone или Item классов.
    """
    class Test:
        def __init__(self):
            self.quantity = 10

    test = Test()
    with pytest.raises(ValueError) as excinfo:
        phone_samsung_16000_4_3.__add__(test)
    assert str(excinfo.value) == 'Можно складывать только экземпляры классов Item и Phone'


def test_number_of_sim(phone_iphone14_120000_5_2):
    """ Проверка количества сим-карт """
    assert phone_iphone14_120000_5_2.number_of_sim == 2

    phone_iphone14_120000_5_2.number_of_sim = 3
    assert phone_iphone14_120000_5_2.number_of_sim == 3

    # Проверка, что количество сим-карт больше 0
    with pytest.raises(ValueError) as excinfo:
        phone_iphone14_120000_5_2.number_of_sim = 0
    assert str(excinfo.value) == 'Количество физических SIM-карт должно быть больше нуля.'
    with pytest.raises(ValueError) as excinfo:
        phone_iphone14_120000_5_2.number_of_sim = -1
    assert str(excinfo.value) == 'Количество физических SIM-карт должно быть больше нуля.'

    # Проверка, что количество сим-карт целочисленно
    with pytest.raises(ValueError) as excinfo:
        phone_iphone14_120000_5_2.number_of_sim = 1.5
    assert str(excinfo.value) == 'Количество физических SIM-карт должно быть целым числом.'
