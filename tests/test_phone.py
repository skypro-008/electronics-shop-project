import pytest


@pytest.mark.parametrize('name, price, quantity, number_of_sim, expected_result', [
    ('IPhone', 100_000, 3, 1, "Phone('IPhone', 100000, 3, 1)"),
    ('Samsung', 50_000, 6, 2, "Phone('Samsung', 50000, 6, 2)"),
    ('Xiaomi', 40_000, 8, 2, "Phone('Xiaomi', 40000, 8, 2)"),
])
def test_repr(phone, name, price, quantity, number_of_sim, expected_result):
    phone.name = name
    phone.price = price
    phone.quantity = quantity
    phone.number_of_sim = number_of_sim

    assert repr(phone) == expected_result
