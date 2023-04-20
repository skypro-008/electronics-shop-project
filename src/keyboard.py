from src.item import Item


class MixinKeyLang:
    """Класс миксин для ввода раскладки клавиатуры"""
    pass

class KeyBoard(Item, MixinKeyLang):
    pass
#super().__init__()
