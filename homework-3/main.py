from src.item import Item

if __name__ == '__main__':
    item1 = Item("Смартфон", 10000, 20)

    assert repr(item1) == "Item('Смартфон', 10000, 20)"
    assert str(item1) == 'Смартфон'
