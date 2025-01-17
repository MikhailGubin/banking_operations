import os
from src.utils import read_json_file, PATH_TO_FILE
from unittest.mock import patch, mock_open
import json


def test_read_json_file(transactions_for_generate: list) -> None:
    """ Проверяет работу функции read_json_file """
    transactions_list = transactions_for_generate
    json_transactions_list = json.dumps(transactions_list)

    mocked_open = mock_open(read_data= f'{json_transactions_list}')

    with patch('builtins.open', mocked_open):
        result = read_json_file(PATH_TO_FILE)

    assert result == transactions_list
    mocked_open.assert_called_once_with(PATH_TO_FILE)


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


def test_read_json_file_value_error() -> None:
    """
    Проверяет работу функции read_json_file при подаче
    неправильных значений на декодирование JSON-файла
    """
    mocked_open = mock_open(read_data='John')
    with patch('builtins.open', mocked_open):
        result = read_json_file(PATH_TO_FILE)
    assert result is None
    mocked_open.assert_called_once_with(PATH_TO_FILE)
