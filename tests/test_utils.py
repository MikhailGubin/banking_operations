import pytest
import os
from src.utils import read_json_file
from unittest.mock import patch, mock_open


def test_read_json_file() -> None:
    """ Проверяет работу функции read_json_file """
    pass


def test_read_json_file_wrong_path() -> None:
    """
    Проверяет, что функция read_json_file выдаёт пустой список,
    если JSON-файл со списком не найден
    """
    path_to_file = os.path.join(os.path.dirname(__file__), "..", "data1", "operations.json")
    assert read_json_file(path_to_file) == []



def test_read_json_file_empty() -> None:
    """
    Проверяет, что функция read_json_file выдаёт пустой список,
    если JSON-файл содержит не список
    """
    # mock_file = mock_open.return_value.__enter__.return_value
    # mock_file.read.return_value = ''
    mocked_open = mock_open(read_data = '[{"id": 1, "amount": "100.0"}]')
    with patch('builtins.open', mock_open):
        result = read_json_file(f"banking_operations\src\..\data\operations.json")
    assert  result == []
    # mock_open.assert_called_once_with('test.txt', 'r')
