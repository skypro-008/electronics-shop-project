class LanguageMixin:

    def change_lang(self):
        self._index += 1
        if self._index >= len(self._langauge_list):
            self._index = 0

    @property
    def language(self):
        return self._langauge_list[self._index]