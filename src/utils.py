import json
import logging
import os

# Получаю абсолютный путь к корневой директории проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Задаю путь к файлу с транзакциями в формате JSON
PATH_TO_FILE = os.path.join(BASE_DIR, "data", "operations.json")
# Задаю путь к файлу utils.log в директории logs
LOG_PATH = os.path.join(BASE_DIR, "logs", "utils.log")


logger_utils = logging.getLogger(__name__)
file_handler_utils = logging.FileHandler(LOG_PATH, mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_utils.setFormatter(file_formatter)
logger_utils.addHandler(file_handler_utils)
logger_utils.setLevel(logging.DEBUG)


def read_json_file(path: str) -> list:
    """
    Возвращает список словарей с данными о финансовых транзакциях из
    JSON-файла
    """
    logger_utils.info("Начало работы функции read_json_file")
    try:
        with open(path) as json_file:

            try:
                transactions_list = json.load(json_file)
            except json.JSONDecodeError:
                logger_utils.error("Невозможно декодировать JSON-данные")
                print("\nНевозможно декодировать JSON-данные")
                return []

    except FileNotFoundError:
        logger_utils.error("JSON-файл не найден")
        print("\nФайл не найден")
        return []

    if not transactions_list:
        logger_utils.error("JSON-файл содержит пустой список")
        print("\nФайл содержит пустой список")
        return []
    elif type(transactions_list) is not list:
        logger_utils.error("Тип объекта в JSON-файле не список")
        print("\nТип объекта в файле не список")
        return []
    logger_utils.info("Функции read_json_file успешно завершила работу")
    return transactions_list


if __name__ == "__main__":
    print(read_json_file(PATH_TO_FILE))
