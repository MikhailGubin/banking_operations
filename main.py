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

if __name__ == "__main__":
    # # Visa Platinum 8990922113665229 - пример банковской карты
    # print(get_mask_card_number(8990922113665229))
    # # Счет 11776614605963066702 - пример банковского счета
    # print(get_mask_account(11776614605963066702))
    # pprint.pprint(read_json_file(PATH_TO_FILE), width=85, indent=4)
    #
    # print(mask_account_card(bank_card_or_account_number))
    # print(get_date("2019-07-03T18:35:29.512364"))
    # pprint.pprint(filter_by_state(banking_operations_info), width=85, indent=4)
    # pprint.pprint(sort_by_date(banking_operations_info, decreasing=False), width=85, indent=4)
    #
    # usd_transactions = filter_by_currency(transactions_for_generate, "USD")
    # for _ in range(2):
    #     pprint.pprint(next(usd_transactions), width=85, indent=4)
    #
    # descriptions = transaction_descriptions(transactions_for_generate)
    # for _ in range(3):
    #     print(next(descriptions))
    #
    # for card_number in card_number_generator(11, 20):
    #     print(card_number)

    # Получаю абсолютный путь к корневой директории проекта
    # BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # # Задаю путь к файлу masks.log в директории logs
    # LOG_PATH = os.path.join(BASE_DIR, "logs", "main.log")
    #
    # logger_masks = logging.getLogger(__name__)
    # file_handler_masks = logging.FileHandler(LOG_PATH, mode="w")
    # file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    # file_handler_masks.setFormatter(file_formatter)
    # logger_masks.addHandler(file_handler_masks)
    # logger_masks.setLevel(logging.DEBUG)

    # Создаю флаги проверки ответов Пользователя
    flag_answer_1 = True
    flag_answer_2 = True
    # Создаю список со словарями для записи данных
    bank_transactions = [{}]

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
            bank_transactions = read_json_file(PATH_TO_FILE)
        elif choose_data_format == "2":
            print("Для обработки выбран CSV-файл")
            bank_transactions = read_csv_file(PATH_TO_CSV_FILE)
        elif choose_data_format == "3":
            print("Для обработки выбран XLSX-файл")
            bank_transactions = read_excel_file(PATH_TO_EXCEL_FILE)
        else:
            print("Введён неверный номер пункта меню")
            flag_answer_1 = True
            continue
    # pprint.pprint(bank_transactions[0:4], width=85, indent=4)

    while flag_answer_2:

        flag_answer_2 = False
        print("Введите статус, по которому необходимо выполнить фильтрацию. "
              "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")

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

        bank_transactions = filter_by_state(bank_transactions, choose_transactions_state)

    filter_for_date = input("Отсортировать операции по дате? Да/Нет\n")

    if filter_for_date.lower() == "да":
        flag_decrease = input("Отсортировать по возрастанию или по убыванию? (по возрастанию / по убыванию)\n")

        if flag_decrease.lower() == "по возрастанию":
            flag_decrease_bool = False
        elif flag_decrease.lower() == "по убыванию":
            flag_decrease_bool = True
        else:
            print("Неправильно введены данные, производится сортировка по убыванию")
            flag_decrease_bool = True

        bank_transactions = sort_by_date(bank_transactions, decreasing=flag_decrease_bool)

    elif filter_for_date.lower() == "нет":
        print("Банковские операции по дате не отсортированы")
    else:
        print("Введено неправильное значение. Банковские операции по дате не отсортированы")


    # pprint.pprint(operations_filtered_by_date[0], width=85, indent=4)
    # pprint.pprint(operations_filtered_by_date[1], width=85, indent=4)
    # pprint.pprint(operations_filtered_by_date[2], width=85, indent=4)

    filter_for_currency = input("Выводить только рублевые транзакции? Да/Нет\n")
    if filter_for_currency.lower() == "да":
        print("Выводятся только рублевые транзакции")
        bank_transactions = [next(filter_by_currency(bank_transactions, "RUB"))
                             for transaction in bank_transactions]
    else:
        print("Выводятся транзакции во всех валютах")

    filter_for_word = input("Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")

    if filter_for_word.lower() == "да":
        word_for_searching = input("Введите слово для поиска \n")
        bank_transactions = get_transaction_by_string(bank_transactions, word_for_searching)
    else:
        print("Список транзакций по определенному слову не отсортирован")

    print("Распечатываю итоговый список транзакций...\n"
          f"Всего банковских операций в выборке: {len(bank_transactions)}")
    pprint.pprint(bank_transactions, width=85, indent=4)

