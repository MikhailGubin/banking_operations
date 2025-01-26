import re

from src.search_and_counter import count_operations_in_categories, get_transaction_with_string
from tests.conftest import transactions_for_generate


def test_get_transaction_with_string(transactions_for_generate: list) -> None:
    """ Проверяет работу функции count_operations_in_categories"""

    required_string = re.compile(r'орг\w+')
    assert get_transaction_with_string(transactions_for_generate, required_string) == [{
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
        }
    ]


def test_count_operations_in_categories(transactions_for_generate: list) -> None:
    """ Проверяет работу функции count_operations_in_categories"""
    bank_categories = ["Перевод со счета на счет", "Перевод с карты на карту"]

    assert count_operations_in_categories(transactions_for_generate, bank_categories) == (
        {'Перевод со счета на счет': 2, 'Перевод с карты на карту': 1})
