import pytest
import functools

from src.decorators import my_function

def test_my_function():
    result = my_function(1, 2)
    assert result == 3

def test_log_message(capsys):
    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "my_function ok\n"
