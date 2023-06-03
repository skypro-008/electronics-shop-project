import pytest

from src.keyboard import Keyboard


@pytest.fixture
def keyboard1():
    return Keyboard('Motospeed GK82 Red Switch', 5590, 4)


def test_init(keyboard1):
    assert keyboard1.name == 'Motospeed GK82 Red Switch'
    assert keyboard1.price == 5590
    assert keyboard1.quantity == 4
    assert keyboard1.language == 'EN'

    with pytest.raises(AttributeError):
        keyboard1.language = 'RU'

    assert Keyboard.pay_rate == 1.0
    assert Keyboard.all[-1] == keyboard1


def test_change_lang(keyboard1):
    keyboard1.change_lang()
    assert keyboard1.language == 'RU'
    keyboard1.change_lang()
    assert keyboard1.language == 'EN'
    keyboard1.change_lang().change_lang()
    assert keyboard1.language == 'EN'
    with pytest.raises(TypeError):
        keyboard1.change_lang('RU')
    assert isinstance(keyboard1.change_lang(), Keyboard)

