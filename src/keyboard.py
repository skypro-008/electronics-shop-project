from src.item import Item


class Mix_Language:
    """
    класс миксин для хранения и изменения раскадки клавиатуры
    """
    def __init__(self, en, ru):
        self._EN = en
        self._RU = ru
        self._language = self._EN

    @property
    def language(self):
        return self._language


    def change_lang(self):
        if self._language == self._EN:
            self._language = self._RU
        else:
            self._language = self._EN
        return self


class Keyboard(Item, Mix_Language):

    """
    класс для смены языка клавиатуры
    """
    def __init__(self, name: str, price: float, quantity: int, language="EN") -> None:
        super().__init__(name, price, quantity)
        Mix_Language.__init__(self, 'EN', 'RU')
        self._language = language

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}', {self.price}, {self.quantity}, {self.language}"

    def __str__(self):
        return f"{self.name}"

