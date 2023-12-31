from src.keyboard import Keyboard
import unittest


class TestKeyboard(unittest.TestCase):
    kb = Keyboard('Dark Project KD87A', 9600, 5)

    def test_change_lang(self):
        self.assertEqual(str(self.kb.language), "EN")

        self.kb.change_lang()
        self.assertEqual(str(self.kb.language), "RU")

        self.kb.change_lang()
        self.assertEqual(str(self.kb.language), "EN")
