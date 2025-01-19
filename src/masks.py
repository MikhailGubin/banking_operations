import os
import logging


# Получаю абсолютный путь к корневой директории проекта
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Задаю путь к файлу masks.log в директории logs
LOG_PATH =os.path.join(BASE_DIR, 'logs', 'masks.log')


logging.basicConfig(
    filename = LOG_PATH,
    filemode= 'w',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
)
logger = logging.getLogger(__name__)


def get_mask_card_number(card_number: str | int) -> str:
    """Маскирует номер банковской карты."""
    logger.info("Начало работы функции get_mask_card_number")
    card_number_str = str(card_number)
    if not card_number_str.isdigit() or len(card_number_str) != 16:
        try:
            raise ValueError("Неправильно введен номер карты")
        except ValueError:
            logger.error("Неправильно введен номер карты")

    logger.info("Функция get_mask_card_number успешно завершила работу")
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: str | int) -> str:
    """Маскирует номер банковского счета."""
    logger.info("Начало работы функции get_mask_account")
    account_number_str = str(account_number)
    if not account_number_str.isdigit() or len(account_number_str) != 20:
        try:
            raise ValueError("Неправильно введен номер счёта")
        except ValueError:
            logger.error("Неправильно введен номер счёта")

    logger.info("Функция get_mask_card_number успешно завершила работу")
    return "**" + account_number_str[-4:]
