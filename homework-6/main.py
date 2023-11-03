from src.item import Item
import os

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv(os.path.join('..', 'scr', 'items.csv'))
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv(os.path.join('..', 'scr', 'test_items.csv'))
    # InstantiateCSVError: Файл item.csv поврежден
