import pytest
import functools
from freezegun import freeze_time
from typing import Any
from src.decorators import my_function, log


def test_my_function() -> None:
    """
    Проверяет работу декоратора log
    """
    result = my_function(1, 2)
    assert result == 3

@freeze_time("2023-01-01")
def test_log_message(capsys: Any) -> None:
    """
    Проверяет вывод сообщений в декораторе log
    """
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok, result: 3\nstart - 1672531200.0; stop - 1672531200.0\n"


@freeze_time("2023-01-01")
def test_log_read_in_file() -> None:
    """
    Проверяет вывод сообщений декоратором log в файле

    """

    @log(filename="function_log")
    def sum_numbers(x, y):
        """
        Складывает два числа
        """
        return x + y

    sum_numbers(1, 2)
    with open(f'function_log.txt', 'r', encoding='utf-8') as file:
        result = file.read()
    assert result == "sum_numbers ok, result: 3\nstart - 1672531200.0; stop - 1672531200.0\n"


@freeze_time("2023-01-01")
def test_log_error(capsys: Any) -> None:
    """
    Проверяет вывод сообщений в декораторе log
    """
    with pytest.raises(Exception):
        my_function("1", 2)


@freeze_time("2023-01-01")
def test_log_error(capsys: Any) -> None:
    """
    Проверяет вывод сообщений в декораторе log
    """
    with pytest.raises(Exception):
        my_function(1, )





