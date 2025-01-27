from src.masks import get_mask_account, get_mask_card_number
import re


def mask_account_card(number_of_card_or_check: str) -> str:
    """Возвращает строку с замаскированным номером карты и счета"""
    name_of_card_or_check = ""
    digits_of_card_or_check = ""

    for i in range(len(number_of_card_or_check)):
        if number_of_card_or_check[i].isdigit():
            name_of_card_or_check = number_of_card_or_check[:i]
            digits_of_card_or_check = number_of_card_or_check[i:]
            break

    if "счет " in name_of_card_or_check.lower() and len(digits_of_card_or_check) == 20:
        return f"{name_of_card_or_check}{get_mask_account(digits_of_card_or_check)}"

    elif (
        "maestro " in name_of_card_or_check.lower()
        or "mastercard " in name_of_card_or_check.lower()
        or "visa " in name_of_card_or_check.lower()
        and len(digits_of_card_or_check) == 16
    ):

        return f"{name_of_card_or_check}{get_mask_card_number(digits_of_card_or_check)}"

    else:
        raise ValueError("Неправильно введен номер счёта")


def get_date(date_and_time: str) -> str:
    """ "возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""
    # Пример даты:2023-06-27T19:53:05Z;25820
    pattern = r"\d{4}[-]\d{2}[-]\d{2}[T]\d{2}[:]\d{2}[:]\d{2}\S+"
    dates = re.findall(pattern, date_and_time)
    if not dates:
        raise ValueError("Неправильный формат даты")

    return f"{date_and_time[8:10]}.{date_and_time[5:7]}.{date_and_time[:4]}"
