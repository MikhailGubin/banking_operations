from typing import Any

import pandas as pd
import pytest
from unittest.mock import patch
from src.csv_and_excel_readers import read_csv_file, read_excel_file
from src.utils import LOG_PATH


@patch("pandas.read_csv")
def test_read_csv_file(mock_read: Any) -> None:
    """ Проверяет работу функции read_csv_file"""
    mock_read.return_value = pd.DataFrame({"Yes":[1,2], "No": [3, 4]})
    assert read_csv_file("test.csv") == [{'No': 3, 'Yes': 1}, {'No': 4, 'Yes': 2}]
    mock_read.assert_called_once_with("test.csv", sep=';')


def test_read_csv_file_not_found() -> None:
    """
    Проверяет работу функции read_csv_file,
    когда CSV-файл не найден
    """
    assert read_csv_file("test.csv") == [{}]


@pytest.mark.parametrize(
    "wrong_data_in_file",
    [
        ({"Yes": [1, 2, 3], "No": [3, 4]}),
        ({"Yes", "No"}),
        ()
    ]
)
@patch("pandas.read_csv")
def test_read_csv_file_wrong_data(mock_read: Any, wrong_data_in_file: dict) -> None:
    """
    Проверяет работу функции read_csv_file,
    когда файл содержит неверные данные
    """
    mock_read.return_value = wrong_data_in_file
    assert read_csv_file("test.csv") == [{}]
    # mock_read.assert_called_once_with("test.csv", sep=';')


def test_read_csv_file_wrong_format() -> None:
    """
    Проверяет работу функции read_csv_file,
    когда файл на вход подаётся файл другого формата
    """
    # LOG_PATH - путь к файлу logs.utils.log
    assert read_csv_file(LOG_PATH) == [{}]


@patch("pandas.read_excel")
def test_read_excel_file(mock_read: Any) -> None:
    """ Проверяет работу функции read_excel_file"""
    mock_read.return_value = pd.DataFrame({"Yes": [1, 2], "No": [3, 4]})
    assert read_excel_file("test.xlsx") == [{'No': 3, 'Yes': 1}, {'No': 4, 'Yes': 2}]
    mock_read.assert_called_once_with("test.xlsx")


def test_read_excel_file_not_found() -> None:
    """
    Проверяет работу функции read_excel_file,
    когда Excel-файл не найден
    """
    assert read_excel_file("test.xlsx") == [{}]


@pytest.mark.parametrize(
    "wrong_data_in_file",
    [
        ({"Yes": [1, 2, 3], "No": [3, 4]}),
        ({"Yes", "No"}),
        ({})
    ]
)
@patch("pandas.read_csv")
def test_read_csv_file_wrong_data(mock_read: Any, wrong_data_in_file: dict) -> None:
    """
    Проверяет работу функции read_excel_file,
    когда файл содержит неверные данные
    """
    mock_read.return_value = wrong_data_in_file
    assert read_excel_file("test.xlsx") == [{}]
    # mock_read.assert_called_once_with("test.xlsx")


def test_read_excel_file_wrong_format() -> None:
    """
    Проверяет работу функции read_excel_file,
    когда файл на вход подаётся файл другого формата
    """
    # LOG_PATH - путь к файлу logs.utils.log
    assert read_excel_file(LOG_PATH) == [{}]
