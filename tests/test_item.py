import pytest

from src.item import Item


@pytest.mark.parametrize(
    "nm, pr, qt, disc", [("TV", 50_000, 10, 0.8), ("Tablet", 1500, 20, 1.2), ("Calculator", 500, 150, 0.9)]
)
def test_item(nm, pr, qt, disc):
    item = Item(nm, pr, qt)
    assert item.name == nm
    assert item.price == pr
    assert item.quantity == qt
    assert item.calculate_total_price() == pr * qt
    Item.pay_rate = disc
    item.apply_discount()
    assert item.price == pr * disc
