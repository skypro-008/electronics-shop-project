from src.item import Item


def test_exceptions_with_non_existfile():
    assert Item.instantiate_from_csv('filenotexist') == 'Отсутствует файл filenotexist'

def test_exceprion_with_instantiate_file():
    assert Item.instantiate_from_csv('!wrongfile') == '!wrongfile повреждён'