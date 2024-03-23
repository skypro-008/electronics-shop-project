import os
import sys

current_directory = os.path.dirname(os.path.abspath(__file__))
parent_directory = os.path.join(current_directory, '..')
sys.path.append(parent_directory)



from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)
    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
