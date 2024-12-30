import os
from functools import wraps
from time import time
from typing import Any, Optional, Callable



def log(filename: Optional[str] = None) -> Callable:
    """
    Логироует начало и конец выполнения функции, а также ее результаты
    или возникшие ошибки
    """
    def decorator(func: Any) -> Any:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                time_start = time()
                result = func(*args, **kwargs)
                time_stop = time()

            except Exception as e:
                message = (f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n"
                           f"start - {time_start}; stop - {time_stop}")

            else:
                message = f"{func.__name__} ok, result: {result}\nstart - {time_start}; stop - {time_stop}"
            if filename:
                with open(f"{filename}.txt", 'w', encoding='utf-8') as file:
                    file.write(message + "\n")
            else:
                print(message)

            return result
        return wrapper
    return decorator

@log(filename=None)
def my_function(x, y):
    """
    Складывает два числа
    """
    return x + y

if __name__ == "__main__":
    result = my_function(1, 2)
    assert result == 3

