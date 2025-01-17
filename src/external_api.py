import os
import requests
from dotenv import load_dotenv
from src.utils import read_json_file, PATH_TO_FILE



BASE_URL = 'https://api.apilayer.com/exchangerates_data/convert'
# URL для сайта Exchange Rates Data API


def get_amount_of_transaction(bank_transaction: dict) -> float | None:
    """
    Принимает на вход транзакцию и возвращает сумму
    транзакции в рублях
    """
    try:
        currency_code = bank_transaction["operationAmount"]["currency"]["code"]
        amount = bank_transaction["operationAmount"]["amount"]
    except Exception as error_message:
        print('\n', error_message)
        return None

    if currency_code == "RUB":
        return float(amount)
    else:
        load_dotenv()
        apikey = os.getenv('API_KEY')
        headers = {"apikey": f"{apikey}"}
        params = {
            'to': 'RUB',
            'from': currency_code,
            'amount': amount
        }
        try:
            response = requests.get(
            BASE_URL,
            headers=headers,
            params=params
            )
        except requests.exceptions.RequestException:
            print("Ошибка при работе с HTTP запросом")
            return None

        if response.status_code != 200:
            print(f"Получены не правильные данные от API. Status_code = {response.status_code}")
            return None
        answer_api = response.json()
        if 'result' not in answer_api.keys():
            print("Получены не правильные данные от API")
            return None
        print(answer_api)
        return float(answer_api['result'])


if __name__ == "__main__":
    bank_transactions = read_json_file(PATH_TO_FILE)
    bank_transaction = bank_transactions[1]
    print(get_amount_of_transaction(bank_transaction))
