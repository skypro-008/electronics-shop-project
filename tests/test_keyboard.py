import pytest
from src.keyboard import Keyboard


@pytest.fixture
def Logitech_K120():
    return Keyboard("Logitech K120", 2000, 15)


@pytest.fixture
def Razer_Ornata():
    return Keyboard("Razer Ornata", 7000, 10)


def test___str__(Logitech_K120, Razer_Ornata):
    assert str(Logitech_K120) == 'Logitech K120'
    assert str(Logitech_K120) != 'LogitechK120'
    assert str(Razer_Ornata) == 'Razer Ornata'


def test_language(Logitech_K120, Razer_Ornata):
    assert str(Logitech_K120.language) == "EN"
    Razer_Ornata.language = "RU"
    assert str(Razer_Ornata.language) != "EN"
    assert str(Razer_Ornata.language) == "RU"
    with pytest.raises(AttributeError):
        Logitech_K120.language = "TH"

def test_change_lang(Logitech_K120, Razer_Ornata):
    assert str(Logitech_K120.language) == "EN"
    Logitech_K120.change_lang()
    assert str(Logitech_K120.language) == "RU"
