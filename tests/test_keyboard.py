from src.keyboard import Keyboard


k1 = Keyboard('test_1', 1000, 50)
k2 = Keyboard('test_2', 10000, 5)


def test_keyboard_init():
    assert k1.name == 'test_1'
    assert k2.name == 'test_2'
    assert k1.price == 1000
    assert k2.price == 10000
    assert k1.quantity == 50
    assert k2.quantity == 5
    assert k1.language == "EN"
    assert k2.language == "EN"


def test_keyboard_change_language():
    k1.change_lang()
    k2.change_lang().change_lang()
    assert k1.language == "RU"
    assert k2.language == "EN"
