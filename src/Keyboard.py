class LanguageMixin:
    def __init__(self):
        self._language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'EN':
            self._language = 'RU'
        else:
            self._language = 'EN'
        return self


class Keyboard(LanguageMixin):
    def __init__(self, model, baud_rate, num_keys):
        super().__init__()
        self.model = model
        self.baud_rate = baud_rate
        self.num_keys = num_keys

    def __str__(self):
        return self.model

    @LanguageMixin.language.setter
    def language(self, value):
        self._language = value
