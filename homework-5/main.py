from src.keyboard import KeyBoard

if __name__ == '__main__':
    kb = KeyBoard('DarkKD87A', 9600, 5)
    assert str(kb) == "DarkKD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

    kb.language = 'CH'
    # AttributeError: property 'language' of 'KeyBoard' object has no setter
