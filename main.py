import logging
import os
import pprint

from data.data_for_main import bank_card_or_account_number, banking_operations_info, transactions_for_generate
from src.csv_and_excel_readers import PATH_TO_CSV_FILE, PATH_TO_EXCEL_FILE, read_csv_file, read_excel_file
from src.generators import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.search_and_counter import get_transaction_by_string
from src.utils import PATH_TO_FILE, read_json_file
from src.widget import get_date, mask_account_card
from typing import Dict, List, Pattern


def main_input() -> dict:
    arg = input()
    return {"1": arg}


def main_interface() -> dict:
    # Создаю флаги проверки ответов Пользователя
    flag_answer_1 = True
    flag_answer_2 = True

    while flag_answer_1:

        flag_answer_1 = False
        print("""
    Привет! Добро пожаловать в программу работы c банковскими транзакциями.
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла
            """)
        choose_data_format = input()
        if choose_data_format == "1":
            print("Для обработки выбран JSON-файл")
        elif choose_data_format == "2":
            print("Для обработки выбран CSV-файл")
        elif choose_data_format == "3":
            print("Для обработки выбран XLSX-файл")
        else:
            print("Введён неверный номер пункта меню")
            flag_answer_1 = True
            continue

    while flag_answer_2:

        flag_answer_2 = False
        print("Введите статус, по которому необходимо выполнить фильтрацию. "
              "\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

        choose_transactions_state = input().upper()
        if choose_transactions_state == "EXECUTED":
            print("Операции отфильтрованы по статусу 'EXECUTED'")
        elif choose_transactions_state == "CANCELED":
            print("Операции отфильтрованы по статусу 'CANCELED'")
        elif choose_transactions_state == "PENDING":
            print("Операции отфильтрованы по статусу 'PENDING'")
        else:
            print(f"Статус операции '{choose_transactions_state}' недоступен.")
            flag_answer_2 = True
            continue

    filter_for_date = input("Отсортировать операции по дате? Да/Нет\n")
    flag_decrease_bool = True
    if filter_for_date.lower() == "да":
        flag_decrease = input("Отсортировать по возрастанию или по убыванию? (по возрастанию / по убыванию)\n")
        if flag_decrease.lower() == "по возрастанию":
            flag_decrease_bool = False
        elif flag_decrease.lower() == "по убыванию":
            print("Производится сортировка по убыванию")
        else:
            print("Неправильно введены данные, производится сортировка по убыванию")


    elif filter_for_date.lower() == "нет":
        print("Банковские операции по дате не отсортированы")
    else:
        print("Введено неправильное значение. Банковские операции по дате не отсортированы")

    filter_for_currency = input("Выводить только рублевые транзакции? Да/Нет\n")
    if filter_for_currency.lower() == "да":
        print("Выводятся только рублевые транзакции")
    else:
        print("Выводятся транзакции во всех валютах")

    filter_for_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    word_for_searching = ""
    if filter_for_word.lower() == "да":
        word_for_searching = input("Введите слово для поиска \n")
    else:
        print("Список транзакций по определенному слову не отсортирован")

    return     {
        'choose_data_format': choose_data_format,
        'choose_transactions_state': choose_transactions_state,
        'filter_for_date': filter_for_date,
        'filter_for_currency': filter_for_currency,
        'filter_for_word': filter_for_word,
        'flag_decrease_bool': flag_decrease_bool,
        'word_for_searching': word_for_searching
    }

def main_functions(params_for_main: dict) -> List[Dict]:
    """
    Отвечает за основную логику проекта с пользователем
    и связывает функциональности между собой
    """
    # Создаю список со словарями для хранения банковских транзакций
    bank_transactions = [{}]

    # Получаю данные, введенные Пользователем, из словаря params_for_main
    choose_data_format = params_for_main['choose_data_format']
    choose_transactions_state = params_for_main['choose_transactions_state']
    filter_for_date = params_for_main['filter_for_date']
    filter_for_currency = params_for_main['filter_for_currency']
    filter_for_word = params_for_main['filter_for_word']
    flag_decrease_bool = params_for_main['flag_decrease_bool']
    word_for_searching = params_for_main['word_for_searching']

    if choose_data_format == "1":
        bank_transactions = read_json_file(PATH_TO_FILE)
    elif choose_data_format == "2":
        bank_transactions = read_csv_file(PATH_TO_CSV_FILE)
    elif choose_data_format == "3":
        bank_transactions = read_excel_file(PATH_TO_EXCEL_FILE)

    bank_transactions = filter_by_state(bank_transactions, choose_transactions_state)

    if filter_for_date.lower() == "да":
        # Производится сортировка операций по дате
        bank_transactions = sort_by_date(bank_transactions, decreasing=flag_decrease_bool)

    if filter_for_currency.lower() == "да":
        # Будут выводиться только рублевые операции
        bank_transactions = [next(filter_by_currency(bank_transactions, "RUB"))
                             for _ in bank_transactions]

    if filter_for_word.lower() == "да":
        # Производится сортировка операций по слову
        bank_transactions = get_transaction_by_string(bank_transactions, word_for_searching)

    return bank_transactions


def get_final_results(transactions_list: list[dict]) -> None:
    """ Выводит результаты работы программы """
    if transactions_list == [{}]:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        number_operations = len(transactions_list)
        print(f"Распечатываю итоговый список транзакций...\nВсего банковских операций в выборке: {number_operations}")
        pprint.pprint(transactions_list, width=85, indent=4)

if __name__ == "__main__":
    args_for_main = main_interface()
    transactions_list = main_functions(args_for_main)
    get_final_results(transactions_list)
