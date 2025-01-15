import json
import os
import requests
from dotenv import load_dotenv
from src.utils import read_json_file


def get_amount_of_transaction(transaction: dict) -> float:
    """
    Принимает на вход транзакцию и возвращает сумму
    транзакции в рублях
    """
    currency_code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]

    if currency_code == "RUB":
        return float(amount)
    else:
        load_dotenv()
        apikey = os.getenv('API_KEY')
        headers = {"apikey": f"{apikey}"}

        response = requests.get(
        f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}",
        headers=headers
        )
        answer_api = response.json()
        return float(answer_api['result'])


if __name__ == "__main__":
    path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
    transactions = read_json_file(path_to_file)
    transaction = transactions[2]

    print(get_amount_of_transaction(transaction))
