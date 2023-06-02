""" KeyBoard class module """
from src.item import Item


class LanguageMixin:
    """
    A mixin class that provides language functionality.

    Attributes:
        _language (str): The current language of the mixin.

    Methods:
        language: Get the current language.
        change_lang: Change the language of the mixin.
    """

    def __init__(self):
        """
        Initializes a new instance of the LanguageMixin class.
        The initial language is set to 'EN'.
        """
        self._language = 'EN'

    @property
    def language(self):
        """
        Get the current language.

        Returns:
            str: The current language.
        """
        return self._language

    def change_lang(self):
        """
        Change the language of the mixin.

        If the current language is 'EN', it changes it to 'RU',
        and vice versa.

        Returns:
            LanguageMixin: The LanguageMixin object itself.
        """
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self


class KeyBoard(Item, LanguageMixin):
    """
    A class representing a keyboard.

    Inherits from:
        Item: The base class for items.
        LanguageMixin: A mixin class for language functionality.

    Attributes:
        _name (str): The name of the keyboard.
        price (float): The price of the keyboard.
        quantity (int): The quantity of the keyboard.
    """
