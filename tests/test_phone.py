import pytest
from src import phone


def test_constructor():
    ph1 = phone.Phone("iPhone 14", 150000, 5, 2)

    assert str(ph1) == "iPhone 14"
    assert repr(ph1) == "Phone('iPhone 14', 150000, 5, 2)"
    with pytest.raises(ValueError):
        ph2 = phone.Phone("Xiomi Redme 9 Note", 15000, 10, 0)
