from abc import ABC, abstractmethod


class Item(ABC):

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class MixinLog:
    def __init__(self, name, price, quantity, language):
        super().__init__(name, price, quantity)
        self.language = language

    def change_lang(self):
        return f'{self.language} RU'


class KeyBoard(Item, MixinLog):
    def __init__(self, name, price, quantity, language='EN'):
        super().__init__(name, price, quantity)
        self.language = language
