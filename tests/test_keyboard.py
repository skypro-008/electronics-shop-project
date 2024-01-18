from src.item import Item
from src.keyboard import Keyboard

kb = Keyboard('Dark Project KD87A', 9600, 5)

def test_keyboard_init():
    """
    Тест создания экземпляра класса Keyboard.
    :param name: Название товара.
    :param price: Цена за единицу товара.
    :param quantity: Количество товара в магазине.
    :param language: Раскладка клавиатуры
    """
    assert kb.name == 'Dark Project KD87A'
    assert kb.price == 9600
    assert kb.quantity == 5
    assert kb.language == "EN"

def test_change_lang():
    """
    Тест смены раскладки клавиатуры.
    """
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"