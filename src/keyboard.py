class Developer:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.language = 'EN'
    def __str__(self):
        return f'{self.name}'

    @property
    def languages(self):
        return self.language


class MixinLog:
    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
            return self
        else:
            self.language = 'EN'
            return self


class Keyboard(Developer, MixinLog):
    pass