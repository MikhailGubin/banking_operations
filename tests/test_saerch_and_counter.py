import re
from typing import Any

import pytest

from src.search_and_counter import count_operations_in_categories, get_transaction_by_string


# transactions_for_generate - фикстура из модуля conftest.py
def test_get_transaction_by_string(transactions_for_generate: list) -> None:
    """
    Проверяет работу функции count_operations_in_categories,
    когда строка находится в значении ключа 'description'
    """
    required_string = r"орг\w+"
    assert get_transaction_by_string(transactions_for_generate, required_string) == [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
        {
            "id": 594226727,
            "state": "PENDING",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб."}},
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_get_transaction_by_string_state(transactions_for_generate: list) -> None:
    """
    Проверяет работу функции count_operations_in_categories,
    когда строка находится в значении ключа 'state'
    """
    # required_string = re.compile(r'P\w+')
    required_string = "Перевод"
    list_of_transactions = get_transaction_by_string(transactions_for_generate, required_string)
    assert list_of_transactions[-2:] == [
        {
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "id": 594226727,
            "operationAmount": {"amount": "67314.70", "currency": {"code": "RUB", "name": "руб."}},
            "state": "CANCELED",
            "to": "Счет 14211924144426031657",
        },
        {
            "date": "2018-09-12T21:27:25.241689",
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "id": 594226727,
            "operationAmount": {"amount": "67314.70", "currency": {"name": "руб."}},
            "state": "PENDING",
            "to": "Счет 14211924144426031657",
        },
    ]


def test_get_transaction_by_string_empty_string(transactions_for_generate: list) -> None:
    """
    Проверяет работу функции count_operations_in_categories, когда
    на вход функции передаётся пустая строка
    """
    assert get_transaction_by_string(transactions_for_generate, "") == [{}]


@pytest.mark.parametrize("wrong_string", [{}, 23])
def test_get_transaction_by_string_wrong_string(transactions_for_generate: list, wrong_string: Any) -> None:
    """
    Проверяет работу функции count_operations_in_categories, когда
    на вход функции передается не правильный тип данных для строки
    """
    assert get_transaction_by_string(transactions_for_generate, wrong_string) == [{}]


def test_get_transaction_by_string_if_no_string(transactions_for_generate: list) -> None:
    """
    Проверяет работу функции count_operations_in_categories,
    когда нужная строка в списке словарей не найдена
    """
    required_string = re.compile(r"@\w+")
    assert get_transaction_by_string(transactions_for_generate, required_string) == [{}]


@pytest.mark.parametrize("wrong_dict", [{}, "key"])
def test_get_transaction_by_string_wrong_dict(wrong_dict: Any) -> None:
    """
    Проверяет работу функции count_operations_in_categories,
    когда на вход функции передаются неправильные данные для
    списка словарей
    """
    required_string = re.compile(r"орг\w+")
    assert get_transaction_by_string(wrong_dict, required_string) == [{}]


def test_count_operations_in_categories(transactions_for_generate: list) -> None:
    """Проверяет работу функции count_operations_in_categories"""
    bank_categories = ["Перевод со счета на счет", "Перевод с карты на карту"]
    assert count_operations_in_categories(transactions_for_generate, bank_categories) == (
        {"Перевод со счета на счет": 2, "Перевод с карты на карту": 1}
    )


@pytest.mark.parametrize("wrong_categories", [{}, 23])
def test_count_operations_in_categories_wrong_categories(
    transactions_for_generate: list, wrong_categories: Any
) -> None:
    """
    Проверяет работу функции count_operations_in_categories,
    когда на вход функции передаются неправильные данные для
    списка категорий операций
    """
    assert count_operations_in_categories(transactions_for_generate, wrong_categories) == {}


@pytest.mark.parametrize("wrong_operations_list", [[], {1, 2}])
def test_count_operations_in_categories_wrong_dict(wrong_operations_list: list) -> None:
    """
    Проверяет работу функции count_operations_in_categories,
    когда на вход функции передаются неправильные данные для
    списка словарей с банковскими операциями
    """
    bank_categories = ["Перевод со счета на счет", "Перевод с карты на карту"]
    assert count_operations_in_categories(wrong_operations_list, bank_categories) == {}


def test_count_operations_in_categories_no_required_operations(transactions_for_generate: list) -> None:
    """
    Проверяет работу функции count_operations_in_categories,
    если банковские операции в заданных категориях отсутствуют
    """
    bank_categories = ["Перевод со счета на карту"]
    assert count_operations_in_categories(transactions_for_generate, bank_categories) == {}
