from src.keyboard import MixinLanguage, KeyBoard

import unittest

class MixinLanguageTest(unittest.TestCase):
    def setUp(self):
        self.keyboard = KeyBoard("Sample Keyboard", 10, 100)

    def test_language_property(self):
        expected_language = "EN"
        self.assertEqual(self.keyboard.language, expected_language)

    def test_language_setter(self):
        expected_language = "RU"
        self.keyboard.language = expected_language
        self.assertEqual(self.keyboard.language, expected_language)

    def test_change_lang(self):
        expected_language = "RU"
        self.keyboard.change_lang()
        self.assertEqual(self.keyboard.language, expected_language)
        self.keyboard.change_lang()  # Switching back to "EN"
        self.assertEqual(self.keyboard.language, "EN")


if __name__ == '__main__':
    unittest.main()
