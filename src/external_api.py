import os
import requests
from dotenv import load_dotenv
from src.utils import read_json_file


def get_amount_of_bank_transaction(bank_transaction: dict) -> float | None:
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
        try:
            response = requests.get(
            f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency_code}&amount={amount}",
            headers=headers
            )
        except requests.exceptions.HTTPError:
            print("HTTP Error. Please check the URL.")
        except requests.exceptions.RequestException:
            print("An error occurred. Please try again later.")

        answer_api = response.json()
        return float(answer_api['result'])


if __name__ == "__main__":
    path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
    bank_transactions = read_json_file(path_to_file)
    bank_transaction = bank_transactions[1]

    print(get_amount_of_bank_transaction(bank_transaction))
