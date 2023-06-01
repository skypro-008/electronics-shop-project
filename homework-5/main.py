from src.keyboard import KeyBoard

if __name__ == '__main__':
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"

    try:
        kb.language = 'CH'
    # AttributeError: property 'language' of 'KeyBoard' object has no setter
    except AttributeError:
        print("AttributeError: property 'language' of 'KeyBoard' object has no setter")
