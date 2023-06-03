import pytest
from src.keyboard import KeyBoard

@pytest.fixture
def get_object():
    kb = KeyBoard('Razer Cynosa v2', 5000, 13)
    return kb

def test_str(get_object):
    assert str(get_object) == 'Razer Cynosa v2'

def test_language(get_object):
    assert get_object.language == 'EN'

    get_object.change_lang()
    assert get_object.language == 'RU'

    get_object.change_lang()
    assert get_object.language == 'EN'

    with pytest.raises(AttributeError):
        get_object.language = 'SP'


