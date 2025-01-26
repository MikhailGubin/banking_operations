import re
from typing import List, Dict
from collections import Counter


def get_transaction_with_string(transactions_dicts: List[Dict], string_for_searching: re.Pattern) -> list[dict]:
    """
    Принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка
    """
    # pattern = re.compile(r'\b(\w){7, 8}\b')

    # wrong_flag = True
    # if not string_for_searching:
    #     print("Отсутствует строка поиска")
    # elif type(string_for_searching) is not str:
    #     print("Неправильный тип данных передан вместо строки поиска")
    # elif not transactions_dicts:
    #     print("Пустой список словарей с данными о банковских операциях")
    # elif type(transactions_dicts) is not list:
    #     print("Неправильный тип данных передан вместо списка словарей с банковскими операциями")
    # else:
    #     wrong_flag = False

    # Проверяю все вышеперечисленные условия. Если хотя бы одно выполняется, то функция заканчивает работу.
    # if wrong_flag:
    #     return []

    required_list_with_dicts = []

    for transaction in transactions_dicts:
        # transaction_values = " ".join(transaction.values())
        if re.findall(string_for_searching, transaction['state']):
            required_list_with_dicts.append(transaction)
        elif re.findall(string_for_searching, transaction['description']):
            required_list_with_dicts.append(transaction)

    if not required_list_with_dicts:
        print("Данная строка в описании банковских операций не найдена")

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
        print("Пустой список категорий операций")
    elif type(operations_categories) is not list:
        print("Неправильный тип данных передан вместо списка категорий операций")
    elif not transactions_dicts:
        print("Пустой список словарей с данными о банковских операциях")
    elif type(transactions_dicts) is not list:
        print("Неправильный тип данных передан вместо списка словарей с банковскими операциями")
    else:
        wrong_flag = False

    # Проверяю все вышеперечисленные условия. Если хотя бы одно выполняется, то функция заканчивает работу.
    if wrong_flag:
        return {}

    counted_category = Counter(transaction['description']
                               for transaction in transactions_dicts
                               if transaction['description'] in operations_categories)
    if not counted_category:
        print("Банковские операции в заданных категориях отсутствуют")

    return counted_category


if __name__ == "__main__":
    bank_categories = ["Перевод со счета на счет", "Перевод с карты на карту"]
    print(type(re.compile(r'\b(\w){7, 8}\b')))

