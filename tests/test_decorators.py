import os

import pytest
import functools
from freezegun import freeze_time
from typing import Any
from src.decorators import log, my_function

PATH_TO_TXT = os.path.join(os.path.dirname(__file__), '..', 'data', "function_log.txt")

def test_my_function() -> None:
    """
    Проверяет работу декоратора log
    """

    result = my_function(1, 2)
    assert result == 3


@freeze_time("2023-01-01")
def test_log_read_in_file() -> None:
    """
    Проверяет вывод сообщений декоратором log в файле

    """

    my_function(4, 1)
    # path = os.path.join(os.path.abspath("."), 'data', "function_log.txt")
    with open(PATH_TO_TXT, 'r', encoding='utf-8') as file:
        content = file.read().split("\n")
    assert content[-3:-1] == ['my_function ok, result: 5',
                        'start - 2023-01-01 00:00:00; stop - 2023-01-01 00:00:00']


@freeze_time("2023-01-01")
def test_log_typerror() -> None:
    """
    Проверяет, что декоратор loq корректно
    обрабатывает входные аргументы неправильного типа данных
    """
    my_function(1, "2")
    with open(PATH_TO_TXT, 'r', encoding='utf-8') as file:
        content = file.read().split("\n")
    assert content[-3:-1] == ["my_function error: unsupported operand type(s) for +: 'int' and 'str'. "
                                "Inputs: (1, '2'), {}", "start - 2023-01-01 00:00:00; stop - 2023-01-01 00:00:00"]


@freeze_time("2023-01-01")
def test_log_error() -> None:
    """
    Проверяет, что декоратор loq корректно
    отрабатывает отсутствие нужного количества входных аргументов
    """
    my_function(1, )
    with open(PATH_TO_TXT, 'r', encoding='utf-8') as file:
        content = file.read().split("\n")
    assert content[-3:-1] == ["my_function error: my_function() missing 1 required positional argument: 'y'. "
                                 "Inputs: (1,), {}", "start - 2023-01-01 00:00:00; stop - 2023-01-01 00:00:00"]

@freeze_time("2023-01-01")
def test_log_message(capsys: Any) -> None:
    """
    Проверяет вывод сообщений декоратора log в консоль
    """

    @log(filename=None)
    def my_function(x: int | float, y: int | float) -> int | float:
        """
        Складывает два числа
        """
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == ("my_function ok, result: 3\n"
                            "start - 2023-01-01 00:00:00; stop - 2023-01-01 00:00:00\n")

