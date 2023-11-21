from src.item import Item, filename


def test_exception():
    Item.instantiate_from_csv("ddd")
    assert "Отсутствует файл item.csv"


def test_exception_break_file():
    assert Item.instantiate_from_csv(filename) == "Файл item.csv поврежден"
