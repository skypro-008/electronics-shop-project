from src.item import Item
from config import OPERATIONS_PATH
if __name__ == '__main__':
    item = Item('Телефон', 10000, 5)

    # длина наименования товара меньше 10 символов
    item.name = 'Смартфон'
    assert item.name == 'Смартфон'

    # длина наименования товара больше 10 символов
    item.name = 'СуперСмартфон'
    assert item.name == 'СуперСмарт'
    # Exception: Длина наименования товара превышает 10 символов.

    Item.instantiate_from_csv(OPERATIONS_PATH)  # создание объектов из данных файла
    assert len(Item.all) == 5  # в файле 5 записей с данными по товарам

    item1 = Item.all[0]
    assert item1.name == 'Смартфон'
    assert Item.string_to_number('5') == 5
