from src.keyboard import Keyboard

kb_name = "logitech123"
kb_price = 9.99
kb_quantity = 1


def test_change_lang():
    keyboard = Keyboard(kb_name, kb_price, kb_quantity)
    assert keyboard.layout == "EN"

    keyboard.change_lang()
    assert keyboard.layout == "RU"



def test__init__():
    keyboard = Keyboard(kb_name, kb_price, kb_quantity)
    assert keyboard.name == "logitech123"
    assert keyboard.price == 9.99
    assert keyboard.quantity == 1

