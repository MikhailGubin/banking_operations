import os

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
    @log(filename=None)
    def my_function(x, y):
        """
        Складывает два числа
        """
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == ("my_function ok, result: 3\n"
                            "start - 2023-01-01 00:00:00; stop - 2023-01-01 00:00:00\n")


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

    sum_numbers(2, 1)
    path = os.path.join(os.path.abspath("."), '..', 'data', "function_log.txt")
    with open(path, 'r', encoding='utf-8') as file:
        content = file.read().split("\n")
    assert content[-3:-1] == ['sum_numbers ok, result: 3',
                        'start - 2023-01-01 00:00:00; stop - 2023-01-01 00:00:00']


@freeze_time("2023-01-01")
def test_log_error(capsys: Any) -> None:
    """
    Проверяет вывод сообщений в декораторе log
    """
    with pytest.raises(TypeError):
        my_function("1", 2)
        captured = capsys.readouterr()
        assert captured.out == ("my_function error: unsupported operand type(s) for +: 'int' and 'str'. "
                                "Inputs: (1, '2'), {}\nstart - 2023-01-01 00:00:00; stop - 2023-01-01 00:00:00\n")

@freeze_time("2023-01-01")
def test_log_error(capsys: Any) -> None:
    """
    Проверяет вывод сообщений в декораторе log
    """
    with pytest.raises(Exception):
        my_function(1, )
        captured = capsys.readouterr()
        assert captured.out == ("my_function error: my_function() missing 1 required positional argument: 'y'. "
                                "Inputs: (1,), {}\nstart - 2023-01-01 00:00:00; stop - 2023-01-01 00:00:00\n")
