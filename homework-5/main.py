from src.keyboard import Keyboard

if __name__ == '__main__':
    kb = Keyboard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_layout()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_layout().change_layout()
    assert str(kb.language) == "RU"

    kb.language = 'CH'  # Raises ValueError: Недопустимый язык. Допустимые значения: 'EN', 'RU'

    # AttributeError: property 'language' of 'KeyBoard' object has no setter
