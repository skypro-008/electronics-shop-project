from src.keyboard import Keyboard


kb = Keyboard('Dark Project KD87A', 9600, 5)


class Test_Keyboard:
    '''Класс для тестов класса Keyboard'''

    def test_str(self):
        assert str(kb) == 'Dark Project KD87A'


    def test_init(self):
        assert kb.name == 'Dark Project KD87A'
        assert kb.price == 9600
        assert kb.quantity == 5


    def test_change_lang(self):
        assert kb.language == 'EN'
        kb.change_lang()
        assert kb.language == 'RU'
