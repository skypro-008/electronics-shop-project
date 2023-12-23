import os

import pytest

from src.exception import AllError, InstantiateCSVError

# Получение пути к текущему исполняемому файлу
current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = current_dir[: -(len(current_dir.split("\\")[-1]) + 1)]

# Создание относительного пути к файлу от текущего файла
non_existent_file = os.path.join(base_dir, "retest", "items.csv")
broken_file = os.path.join(base_dir, "data", "broken_file.csv")


@pytest.fixture
def item():
    return InstantiateCSVError


def test_instantiate(item):
    with pytest.raises(AllError):
        item(broken_file)
