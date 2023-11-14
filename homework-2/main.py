from src.item import Item

# Файл 'main.py' подкорректирован под выполнение ТЗ из файла 'README'.

if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.get_name = 'Смартфон'
    assert item.get_name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.get_name = 'СуперСмартфон'
    # В атрибут __name записывается первые 10 символов названия.

    Item.instantiate_from_csv('../src/items.csv')  # создание объектов из данных файла
    assert len(Item.all) == 6  # в файле 1 + 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.get_name == 'СуперСмарт'

    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5
