import pytest

from src.language_mixin import LanguageMixin


@pytest.fixture
def lang_mixin_fixture():
    return LanguageMixin(langs_list=['L1', 'L2'])


def test_language_mixin_language_prop(safe_item_class, lang_mixin_fixture):
    assert lang_mixin_fixture.language == 'L1'


def test_language_mixin_change_lang(safe_item_class, lang_mixin_fixture):
    assert lang_mixin_fixture.language == 'L1'
    assert lang_mixin_fixture.change_lang().language == 'L2'
    assert lang_mixin_fixture.change_lang().language == 'L1'
