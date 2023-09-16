class LanguageMixin:
    def __init__(self, langs_list=None, **kwargs):
        super().__init__(**kwargs)

        self._lang_list = langs_list if langs_list else ['EN']
        self._curr_lang_id = 0

    @property
    def language(self):
        return self._lang_list[self._curr_lang_id]

    def change_lang(self):
        self._curr_lang_id += 1
        if self._curr_lang_id >= len(self._lang_list):
            self._curr_lang_id = 0
        return self
