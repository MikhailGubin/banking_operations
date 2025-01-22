import logging
import os

# Получаю абсолютный путь к корневой директории проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Задаю путь к файлу masks.log в директории logs
LOG_PATH = os.path.join(BASE_DIR, "logs", "masks.log")


logger_masks = logging.getLogger(__name__)
file_handler_masks = logging.FileHandler(LOG_PATH, mode="w")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler_masks.setFormatter(file_formatter)
logger_masks.addHandler(file_handler_masks)
logger_masks.setLevel(logging.DEBUG)


def get_mask_card_number(card_number: str | int) -> str:
    """Маскирует номер банковской карты."""
    logger_masks.info("Начало работы функции get_mask_card_number")
    card_number_str = str(card_number)
    if not card_number_str.isdigit() or len(card_number_str) != 16:
        logger_masks.error("Неправильно введен номер карты")
        raise ValueError("Неправильно введен номер карты")

    logger_masks.info("Функция get_mask_card_number успешно завершила работу")
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: str | int) -> str:
    """Маскирует номер банковского счета."""
    logger_masks.info("Начало работы функции get_mask_account")
    account_number_str = str(account_number)
    if not account_number_str.isdigit() or len(account_number_str) != 20:
        logger_masks.error("Неправильно введен номер счёта")
        raise ValueError("Неправильно введен номер счёта")

    logger_masks.info("Функция get_mask_card_number успешно завершила работу")
    return "**" + account_number_str[-4:]
