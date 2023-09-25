# -*- coding: utf-8 -*-
import pytest
import os
from src import item

def test_instantiate_from_csv_path_errors():
    """Проверка ошибки несуществующего файла csv"""
    path_to_test_csv = os.path.join('1test_csv_file.csv')
    item.Item.CSV_PATH = path_to_test_csv
    with pytest.raises(FileNotFoundError):
        item.Item.instantiate_from_csv()
