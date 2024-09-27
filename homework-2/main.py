import csv
from src.item import Item

if __name__ == '__main__':
    Item.instantiate_from_csv('src/items.csv')  # создание объектов из данных файла

    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'

    assert len(Item.all) == 6  # в файле 5 записей + 1 созданный объект в коде

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5.5








