from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'


import os
"""PROJECT_DIRECTORY хранит абсолютный путь к корневой директории проекта"""
PROJECT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))

if __name__ == '__main__':
    print(PROJECT_DIRECTORY)
    print()