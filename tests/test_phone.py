import pytest
from src.phone import Phone


@pytest.mark.parametrize("sim_count, expected_result", [
    (1, 1),
    (2, 2),
    (0, ValueError),
    (-1, ValueError),
    (1.1, ValueError)
])
def test_Phone_number_of_sim(safe_item_class, sim_count, expected_result):
    if isinstance(expected_result, int):
        phone1 = Phone("", 0, 0, sim_count)
        assert phone1.number_of_sim == expected_result
    else:
        with pytest.raises(expected_result):
            _ = Phone("", 0, 0, sim_count)

        phone1 = Phone("", 0, 0)
        with pytest.raises(expected_result):
            phone1.number_of_sim = sim_count


def test_Phone_add(safe_item_class):
    item1 = safe_item_class("", 0, 5)
    phone1 = Phone("", 0, 10)

    assert item1 + phone1 == 15
