import os
from src.external_api import get_amount_of_transaction
from src.utils import read_json_file
from unittest.mock import patch, mock_open
from dotenv import load_dotenv
import json


def test_get_amount_of_transaction_usd_to_rub() -> None:
    """
    Проверяет работу функции get_amount_of_transaction
    при конвертации валюты из долларов в рубли
    """
    path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
    transactions = read_json_file(path_to_file)
    transaction = transactions[2]
    load_dotenv()
    apikey = os.getenv('API_KEY')

    with patch('requests.get') as mock_get:
        mock_get.return_value.json.return_value = {'success': True,
        'query': {'from': 'USD', 'to': 'RUB', 'amount': 9824.07},
        'info': {'timestamp': 1736973004, 'rate': 102.502027},
        'date': '2025-01-15', 'result': 1006987.08839
        }
        assert get_amount_of_transaction(transaction) == 1006987.08839
        mock_get.assert_called_once_with(
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=9824.07",
                                         headers={'apikey': apikey}
        )

def test_get_amount_of_transaction(transactions_for_generate: list) -> None:
    """
    Проверяет работу функции get_amount_of_transaction
    при подаче на вход суммы в рублях
    """
    transactions_list = transactions_for_generate

    path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
    transactions = read_json_file(path_to_file)
    transaction = transactions[0]
    assert get_amount_of_transaction(transaction) == 31957.58


