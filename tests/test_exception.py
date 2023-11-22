from src.item import Item
from pathlib import Path


def test_exception():
    assert Item.instantiate_from_csv("ddd") == "Отсутствует файл item.csv"


def test_exception_break_file():
    file = Path(Path(__file__).parent.parent, 'src', 'item_test.csv')
    assert Item.instantiate_from_csv(file) == "Файл item.csv поврежден"
