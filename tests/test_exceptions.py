import pytest
from src.item import Item
from src.exceptions import InstantiateCSVError


@pytest.fixture
def item():
    return Item("cake", 5.5, 3)


def test_no_file(item):
    with pytest.raises(FileNotFoundError, match='Отсутствует файл item.csv'):
        item.instantiate_from_csv()


def test_damaged_file(item):
    with pytest.raises(InstantiateCSVError, match='Файл item.csv поврежден'):
        item.instantiate_from_csv()
