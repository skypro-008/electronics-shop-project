from dataclasses import dataclass
from src.item import *


@dataclass
class MixinKeyboard:
    language: str

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        elif self.language == 'RU':
            self.language = 'EN'
        return self.language


class Keyboard(Item, MixinKeyboard):
    def __init__(self, name: str, price: int, quantity: int):
        super().__init__(name, price, quantity)
        self.language = 'EN'
