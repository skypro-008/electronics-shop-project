from src.keyboard import Keyboard, KeyboardMixin

#TestCase для проверки создания объекта класса Keyboard
kb = Keyboard('Dark Project KD87A', 9600, 5)
assert str(kb.name) == "Dark Project KD87A"
assert str(kb.price) == '9600'
assert str(kb.quantity) == '5'
assert str(kb.language) == 'EN'

#TestCase для проверки работы магического метода __str__
assert str(kb.__str__()) == 'Dark Project KD87A'

#TestCase для проверки работы метода changelang()
# Меняем язык на RU
kb.change_lang()
assert str(kb.language) == 'RU'
# Меняем обратно на EN
kb.change_lang()
assert str(kb.language) == "EN"
