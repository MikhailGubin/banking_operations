import json
import os
import requests
from dotenv import load_dotenv


def read_json_file(path: str) -> list:
    """
    Возвращает список словарей с данными о финансовых транзакциях из
    JSON-файла
    """
    try:
        with open(path) as f:
            transactions_list = json.load(f)
    except FileNotFoundError:
        return []
    else:
        if not transactions_list or type(transactions_list) != list:
            return []
        return transactions_list


if __name__ == "__main__":

    path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")

    print(read_json_file(path_to_file))
    print(path_to_file)

    # with open(path, "r", encoding='utf-8') as f: