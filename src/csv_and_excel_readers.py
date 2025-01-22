import csv
import pandas as pd
from typing import List, Dict
import os


# Получаю абсолютный путь к корневой директории проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Задаю путь к файлу с транзакциями в формате CSV
PATH_TO_CSV_FILE = os.path.join(BASE_DIR, "data", "transactions.csv")
# Задаю путь к файлу с транзакциями в формате Excel
PATH_TO_EXCEL_FILE = os.path.join(BASE_DIR, "data", "transactions_excel.xlsx")


def read_csv_file(path_to_file: str) -> List[Dict]:
    """
    Считывает финансовые операций из CSV-файла,
    выдаёт список словарей с транзакциями
    """
    try:
        try:
            df_csv_file = pd.read_csv(path_to_file, sep=";")
        except Exception as error_message:
            print(f"\nВозникла ошибка при чтении CSV-файла. Текст ошибки: \n{error_message}")
            return [{}]
        transactions_dict = df_csv_file.to_dict(orient="records")
    except Exception as error_message:
        print(f"\nВозникла ошибка при записи содержимого CSV-файла в словарь. Текст ошибки: \n{error_message}")
        return [{}]
    if not transactions_dict:
        print("\nВ CSV-файле нет данных")
        return [{}]
    return transactions_dict


def read_excel_file(path_to_file: str) -> List[Dict]:
    """
    Считывает финансовые операций из Excel-файла,
    выдаёт список словарей с транзакциями
    """
    try:
        try:
            df_excel_file = pd.read_excel(path_to_file)
        except Exception as error_message:
            print(f"\nВозникла ошибка при чтении Excel-файла. Текст ошибки: \n{error_message}")
            return [{}]
        transactions_dict = df_excel_file.to_dict(orient="records")
    except Exception as error_message:
        print(f"\nВозникла ошибка при записи содержимого Excel-файла в словарь. Текст ошибки: \n{error_message}")
        return [{}]
    if not transactions_dict:
        print("\nВ Excel-файле нет данных")
        return [{}]
    return transactions_dict


if __name__ == "__main__":
    pd_csv_file = pd.read_csv(PATH_TO_CSV_FILE)
    print(pd_csv_file.head())
    pd_excel_file = pd.read_excel(PATH_TO_EXCEL_FILE)
    print(pd_excel_file.head())
