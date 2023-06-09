from src.item import Item, InstantiateCSVError

if __name__ == '__main__':
    # Файл items.csv отсутствует.
    Item.instantiate_from_csv("../src/not_found_items.csv")
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле items.csv удалена последняя колонка.
    Item.instantiate_from_csv("../tests/without_colum_items.csv")
    # InstantiateCSVError: Файл item.csv поврежден

    # Проверка, что данные с файла без ошибок считываются корректно
    Item.instantiate_from_csv("../src/items.csv")
    print(len(Item.all))
