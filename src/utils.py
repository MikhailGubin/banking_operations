import json
import os


def read_json_file(path: str) -> list | None:
    """
    Возвращает список словарей с данными о финансовых транзакциях из
    JSON-файла
    """
    try:
        with open(path) as json_file:

            try:
                transactions_list = json.load(json_file)
            except json.JSONDecodeError:
                print("Invalid JSON data.")
                return None
            except ValueError:
                print("Invalid JSON data.")
                return None

    except FileNotFoundError:
        print("\nФайл не найден")
        return []
    else:
        if not transactions_list:
            print("\nФайл содержит пустой список")
            return []
        elif type(transactions_list) != list:
            print("\nТип объекта в файле не список")
            return []
        return transactions_list


if __name__ == "__main__":

    path_to_file = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")
    print(read_json_file(path_to_file))
    print(path_to_file)
