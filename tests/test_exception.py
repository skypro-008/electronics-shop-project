import pytest

from exception.exception import InstantiateCSVError
from src.item import Item, filename


def test_exception():
    Item.instantiate_from_csv("ddd")
    assert "Отсутствует файл item.csv"


def test_exception_break_file():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(filename)
