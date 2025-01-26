import os

import requests
from dotenv import load_dotenv

BASE_URL = "https://api.apilayer.com/exchangerates_data/convert"
# URL для сайта Exchange Rates Data API


def get_amount_of_transaction(bank_operation: dict) -> float | None:
    """
    Принимает на вход транзакцию и возвращает сумму
    транзакции в рублях
    """
    try:
        currency_code = bank_operation["operationAmount"]["currency"]["code"]
        amount = bank_operation["operationAmount"]["amount"]
    except Exception as error_message:
        print(f"\nНеправильные входные данные. Код ошибки: {error_message}")
        return None

    if currency_code == "RUB":
        return float(amount)
    else:
        load_dotenv()
        apikey = os.getenv("API_KEY")
        headers = {"apikey": f"{apikey}"}
        params = {"to": "RUB", "from": currency_code, "amount": amount}
        try:
            response = requests.get(BASE_URL, headers=headers, params=params)
        except requests.exceptions.RequestException:
            print("Ошибка при работе с HTTP запросом")
            return None

        if response.status_code != 200:
            print(f"Получены неправильные данные от API. Status_code = {response.status_code}")
            return None
        answer_api = response.json()
        try:
            currency_amount = float("{:.2f}".format(answer_api["result"]))
        except Exception as error_text:
            print(f"\nНекорректные данные в ответе от API. Код ошибки: {error_text}")
            return None

        return currency_amount
