from src.item import Item
import os

# Получение пути к текущему исполняемому файлу
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = current_dir[: -(len(current_dir.split("\\")[-1]) + 1)]

# Создание относительного пути к файлу от текущего файла
non_existent_file = os.path.join(base_dir, "retest", "items.csv")
broken_file = os.path.join(base_dir, "data", "broken_file.csv")

if __name__ == '__main__':
    # Файл new_items.csv отсутствует.
    Item.instantiate_from_csv(non_existent_file)
    # FileNotFoundError: Отсутствует файл item.csv

    # В файле new_items.csv удалена последняя колонка.
    Item.instantiate_from_csv(broken_file)
    # InstantiateCSVError: Файл item.csv поврежден
