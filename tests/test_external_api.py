import os
import pytest
from src.external_api import get_amount_of_transaction
from src.utils import read_json_file
from unittest.mock import patch
from dotenv import load_dotenv
from typing import Any


PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
# Задаю путь к файлу с транзакциями в формате JSON


def test_get_amount_of_transaction_usd_to_rub() -> None:
    """
    Проверяет работу функции get_amount_of_transaction
    при конвертации валюты из долларов в рубли
    """
    transactions = read_json_file(PATH_TO_FILE)
        
    load_dotenv()
    apikey = os.getenv('API_KEY')

    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'success': True,
        'query': {'from': 'USD', 'to': 'RUB', 'amount': 9824.07},
        'info': {'timestamp': 1736973004, 'rate': 102.502027},
        'date': '2025-01-15', 'result': 1006987.08839
        }
        assert get_amount_of_transaction(transactions[2]) == 1006987.08839
        mock_get.assert_called_once_with(
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=9824.07",
                                         headers={'apikey': apikey}
        )


def test_get_amount_of_transaction_eur_to_rub() -> None:
    """
    Проверяет работу функции get_amount_of_transaction
    при конвертации валюты из евро в рубли
    """
    transaction = {
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "EUR",
        "code": "EUR"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  }

    load_dotenv()
    apikey = os.getenv('API_KEY')

    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'success': True,
                                                   'query': {'from': 'EUR', 'to': 'RUB', 'amount': 9824.07},
                                                   'info': {'timestamp': 1736973004, 'rate': 102.502027},
                                                   'date': '2025-01-15', 'result': 1006987.08839
                                                   }
        assert get_amount_of_transaction(transaction) == 1006987.08839
        mock_get.assert_called_once_with(
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=EUR&amount=9824.07",
            headers={'apikey': apikey})


def test_get_amount_of_transaction() -> None:
    """
    Проверяет работу функции get_amount_of_transaction
    при подаче на вход суммы в рублях
    """

    transactions = read_json_file(PATH_TO_FILE)
    transaction = transactions[0]
    assert get_amount_of_transaction(transaction) == 31957.58


@pytest.mark.parametrize(
    "wrong_transaction",
    [(
            {}
    ),
        ({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    #   "operationAmount": {
    #   "amount": "31957.58",
    #   "currency": {
    #     "name": "руб.",
    #     "code": "RUB"
    #   }
    # },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }),
        ({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      # "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  }),
            ({
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        # "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  })])
def test_get_amount_of_transaction_wrong_input_data(wrong_transaction: Any) -> None:
    """
    Проверяет работу функции get_amount_of_transaction
    при подаче на вход неверных данных
    """
    assert get_amount_of_transaction(wrong_transaction) is None


def test_get_amount_of_transaction_http_error() -> None:
    """
    Проверяет работу функции get_amount_of_transaction,
    если полученный ответ от сервера не является корректным
    HTTP-ответом
    """
    pass


def test_get_amount_of_transaction_request_exception() -> None:
    """
    Проверяет работу функции get_amount_of_transaction
    при ошибке с HTTP-запросами
    """
    pass