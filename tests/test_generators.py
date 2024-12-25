import pytest

from src.generators import filter_by_currency, transaction_descriptions


def test_filter_by_currency(transactions_for_generate: list, currency: str = "USD") -> None:
    """"
    Проверяет работу функции filter_by_currency
    """
    currency_transactions = filter_by_currency(transactions_for_generate, currency)

    assert next(currency_transactions) == {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702"
        }
    assert next(currency_transactions) ==  {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }


def test_filter_by_currency_rub(transactions_for_generate: list, currency: str = "RUB") -> None:
    """"
    Проверяет, что функция filter_by_currency корректно фильтрует по заданному
    значению валюты
    """
    generate = filter_by_currency(transactions_for_generate, currency)

    assert next(generate) == {
            "id": 659569852,
            "state": "EXECUTED",
            "date": "2021-05-06T13:41:05.878206",
            "operationAmount": {
                "amount": "97411.39",
                "currency": {
                    "name": "RUB",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Maestro 1596837868705199",
            "to": "Visa Classic 6831982476737658"
        }

def test_filter_by_currency_empty_list() -> None:
    """"
    Проверяет, что функция filter_by_currency корректно
    работает при передаче ей пустого списка
    """
    empty_transaction = filter_by_currency([])
    assert next(empty_transaction) == "Пустой список транзакций"


def test_filter_by_no_currency_in_list(transactions_for_generate: list, currency: str = "EURO") -> None:
    """"
    Проверяет, что функция filter_by_currency корректно
    работает при передаче ей списка, где нет заданной
    валюты
    """
    no_necessary_transaction = filter_by_currency(transactions_for_generate, currency)
    assert next(no_necessary_transaction) == "Транзакции в заданной валюте отсутствуют"