from src.keyboard import KeyBoard


def test__str__():
    """Тестируем инициализацию объекта класса KeyBoard"""
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb) == "Dark Project KD87A"
    assert kb.price == 9600
    assert kb.quantity == 5



def test_change_lang():
    """Тестируем метод change_lang(), меняет язык"""
    kb = KeyBoard('Dark Project KD87A', 9600, 5)
    assert str(kb.language) == "EN"
    kb.change_lang()
    assert str(kb.language) == "RU"

    # Сделали RU -> EN -> RU
    kb.change_lang().change_lang()
    assert str(kb.language) == "RU"
