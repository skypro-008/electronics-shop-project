from src.item import Item

if __name__ == '__main__':
    # Файл item.csv отсутствует.
    Item.instantiate_from_csv("../src/item.csv")
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле item.csv удалена последняя колонка.
    Item.instantiate_from_csv("../src/item2.csv")
    # InstantiateCSVError: Файл item.csv поврежден

