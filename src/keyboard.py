from src.item import Item
from accessify import private

class MixinLan:


    def __init__(self):
        self.language = "EN"

    def change_lang(self):
        if self.language == "EN":
            self.language = "RU"
        else:
            self.language = "EN"
        return self

class Keyboard(Item,MixinLan):

    def __init__(self,name,price,quantity):
        super().__init__(name,price,quantity)


    def __str__(self):
        return f'{self.name}'

