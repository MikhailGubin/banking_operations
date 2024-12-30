import pytest

def log(filename=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(f'{filename}.txt', 'w', encoding='utf-8') as file:
                        file.write(f"{func.__name__} ok\n")
                else:
                    print(f"{func.__name__} ok")

                return result
            except Exception as e:
                if filename:
                    with open(f'{filename}.txt', 'w', encoding='utf-8') as file:
                        file.write(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func.__name__} error: {e}. Inputs: {args}, {kwargs}")

        return wrapper
    return decorator

@log(filename=None)
def my_function(x, y):
    return x + y

if __name__ == "__main__":
    result = my_function(1, 2)
    assert result == 3

# my_function(1, 2)
# Ожидаемый вывод в лог-файл
# mylog.txt
#  при успешном выполнении:
# my_function ok
# Ожидаемый вывод при ошибке:
# my_function error: тип ошибки. Inputs: (1, 2), {}
# Где тип ошибки заменяется на текст ошибки.