from src.CSVError import InstantiateCSVError
from src.item import Item
def test_not_found():
    try:
        Item.instantiate_from_csv("../src/items.csv")
        assert True
    except FileNotFoundError:
        Item.instantiate_from_csv()
        assert True


def test_exception():
    try:
        Item.instantiate_from_csv("../src/items.csv")
        assert True
    except InstantiateCSVError:
        Item.instantiate_from_csv()
        assert False