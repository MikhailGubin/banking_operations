import pytest

from src.generators import filter_by_currency, transaction_descriptions


# @pytest.mark.parametrize(
#     "currency, expected",
#     [
#         ("USD", {
#             "id": 939719570,
#             "state": "EXECUTED",
#             "date": "2018-06-30T02:08:58.425572",
#             "operationAmount": {
#                 "amount": "9824.07",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод организации",
#             "from": "Счет 75106830613657916952",
#             "to": "Счет 11776614605963066702"
#         }),
#         ("USD", {
#             "id": 142264268,
#             "state": "EXECUTED",
#             "date": "2019-04-04T23:20:05.206878",
#             "operationAmount": {
#                 "amount": "79114.93",
#                 "currency": {
#                     "name": "USD",
#                     "code": "USD"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Счет 19708645243227258542",
#             "to": "Счет 75651667383060284188"
#         }),
#         ("RUB", {
#             "id": 659569852,
#             "state": "EXECUTED",
#             "date": "2021-05-06T13:41:05.878206",
#             "operationAmount": {
#                 "amount": "97411.39",
#                 "currency": {
#                     "name": "RUB",
#                     "code": "RUB"
#                 }
#             },
#             "description": "Перевод со счета на счет",
#             "from": "Maestro 1596837868705199",
#             "to": "Visa Classic 6831982476737658"
#         })
#     ],
# )
def test_filter_by_currency(transactions_for_generate: list, currency: str = "USD") -> None:
    """"
    Проверяет работу функции filter_by_currency
    """
    generate = filter_by_currency(transactions_for_generate, currency)

    assert next(generate) == {
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
    assert next(generate) ==  {
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

    assert next(filter_by_currency(transactions_for_generate, currency="RUB")) == {
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
