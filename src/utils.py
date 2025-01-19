import json
import os
import logging


# Получаю абсолютный путь к корневой директории проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Задаю путь к файлу с транзакциями в формате JSON
PATH_TO_FILE = os.path.join(BASE_DIR, "data", "operations.json")
# Задаю путь к файлу utils.log в директории logs
LOG_PATH =os.path.join(BASE_DIR, 'logs', 'utils.log')


logging.basicConfig(
    filename = LOG_PATH,
    filemode= 'w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger(__name__)

def read_json_file(path: str) -> list:
    """
    Возвращает список словарей с данными о финансовых транзакциях из
    JSON-файла
    """
    logger.info('Начало работы функции read_json_file')
    try:
        with open(path) as json_file:

            try:
                transactions_list = json.load(json_file)
            except json.JSONDecodeError:
                logger.error('Невозможно декодировать JSON-данные')
                print("\nНевозможно декодировать JSON-данные")
                return []

    except FileNotFoundError:
        logger.error('JSON-файл не найден')
        print("\nФайл не найден")
        return []

    if not transactions_list:
        logger.error('JSON-файл содержит пустой список')
        print("\nФайл содержит пустой список")
        return []
    elif type(transactions_list) is not list:
        logger.error('Тип объекта в JSON-файле не список')
        print("\nТип объекта в файле не список")
        return []
    logger.info('Функции read_json_file успешно завершила работу')
    return transactions_list


if __name__ == "__main__":
    print(read_json_file(PATH_TO_FILE))
