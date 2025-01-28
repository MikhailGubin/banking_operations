import re
from typing import List, Dict
from collections import Counter

from typing_extensions import Pattern


def get_transaction_by_string(transactions_dicts: List[Dict], string_for_searching: str | Pattern) -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка
    """
    wrong_flag = True
    if not string_for_searching:
        print("\nОтсутствует строка поиска")
    elif not transactions_dicts:
        print("\nПустой список словарей с данными о банковских операциях")
    elif type(transactions_dicts) is not list:
        print("\nНеправильный тип данных передан вместо списка словарей с банковскими операциями")
    else:
        wrong_flag = False

    # Проверяю все вышеперечисленные условия. Если хотя бы одно выполняется, то функция заканчивает работу.
    if wrong_flag:
        return [{}]

    required_list_with_dicts = []

    for transaction in transactions_dicts:

        try:
            if re.findall(string_for_searching, transaction['state'], flags=re.IGNORECASE):
                required_list_with_dicts.append(transaction)
            elif re.findall(string_for_searching, transaction['description'], flags=re.IGNORECASE):
                required_list_with_dicts.append(transaction)
        except Exception as error_message:
            print(f"\nОшибка поиска строки. Сообщение об ошибке:\n{error_message}")
            return [{}]

    if not required_list_with_dicts:
        print("\nДанная строка в описании банковских операций не найдена")
        return [{}]

    return required_list_with_dicts



def count_operations_in_categories(transactions_dicts: List[Dict], operations_categories: list) -> dict:
    """
    Принимает список словарей с данными о банковских операциях
    и список категорий операций, а возвращает словарь, в котором ключи — это
    названия категорий, а значения — это количество операций в каждой категории.
    Категории операций хранятся в поле description
    """
    wrong_flag = True
    if not operations_categories:
        print("\nПустой список категорий операций")
    elif type(operations_categories) is not list:
        print("\nНеправильный тип данных передан вместо списка категорий операций")
    elif not transactions_dicts:
        print("\nПустой список словарей с данными о банковских операциях")
    elif type(transactions_dicts) is not list:
        print("\nНеправильный тип данных передан вместо списка словарей с банковскими операциями")
    else:
        wrong_flag = False

    # Проверяю все вышеперечисленные условия. Если хотя бы одно выполняется, то функция заканчивает работу.
    if wrong_flag:
        return {}

    counted_category = Counter(transaction['description']
                               for transaction in transactions_dicts
                               if transaction['description'] in operations_categories)
    if not counted_category:
        print("\nБанковские операции в заданных категориях отсутствуют")

    return counted_category


if __name__ == "__main__":
    bank_categories = ["Перевод со счета на счет", "Перевод с карты на карту"]
    print(type(re.compile(r'\b(\w){7, 8}\b')))

