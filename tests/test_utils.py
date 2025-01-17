import os
from src.utils import read_json_file, PATH_TO_FILE
from unittest.mock import patch, mock_open
from data.operations_for_tests import data_for_read_json_file
import json


def test_read_json_file(data_for_read_json_file: list) -> None:
    """ Проверяет работу функции read_json_file """
    # Фикстура data_for_read_json_file находится в конце файле operations_for_tests.py
    assert read_json_file(PATH_TO_FILE) == data_for_read_json_file



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
    если JSON-файл содержит пустой список
    """
    mocked_open = mock_open(read_data='[]')
    with patch('builtins.open', mocked_open):
        result = read_json_file(PATH_TO_FILE)
    assert  result == []
    mocked_open.assert_called_once_with(PATH_TO_FILE)


def test_read_json_file_not_list() -> None:
    """
    Проверяет, что функция read_json_file выдаёт пустой список,
    если JSON-файл содержит не список
    """
    mocked_open = mock_open(read_data='{"key": "Value"}')
    with patch('builtins.open', mocked_open):
        result = read_json_file(PATH_TO_FILE)
    assert  result == []
    mocked_open.assert_called_once_with(PATH_TO_FILE)


def test_read_json_file_json_decode_error() -> None:
    """
    Проверяет работу функции read_json_file
    при ошибке декодирования JSON-файла
    """
    mocked_open = mock_open(read_data='{"key: "Value"}')
    with patch('builtins.open', mocked_open):
        result = read_json_file(PATH_TO_FILE)
    assert result is None
    mocked_open.assert_called_once_with(PATH_TO_FILE)
