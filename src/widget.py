from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(number_of_card_or_check: str) -> str:
    """Возвращает строку с замаскированным номером карты и счета"""
    name_of_card_or_check = ""
    digits_of_card_or_check = ""

    for i in range(len(number_of_card_or_check)):
        if number_of_card_or_check[i].isdigit():
            name_of_card_or_check = number_of_card_or_check[:i]
            digits_of_card_or_check = number_of_card_or_check[i:]
            break

    if "счет" in name_of_card_or_check.lower() and len(digits_of_card_or_check) == 20:
        return f"{name_of_card_or_check} {get_mask_account(digits_of_card_or_check)}"

    elif len(digits_of_card_or_check) == 16:
        return f"{name_of_card_or_check} {get_mask_card_number(digits_of_card_or_check)}"

    else:
        return "Неправильно введен номер карты или счёта"


def get_date(date_and_time: str) -> str:
    """ "возвращает строку с датой в формате "ДД.ММ.ГГГГ" ("11.03.2024")"""
    return f"{date_and_time[8:10]}.{date_and_time[5:7]}.{date_and_time[:4]} "
