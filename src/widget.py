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
    if len(date_and_time) != 26:
        raise ValueError("Количество символов в дате меньше 26")

    number = [date_and_time[i] for i in [0, 1, 2, 3, 5, 6, 8, 9, 11, 12, 14, 15, 17, 18, 20, 21]]
    digits_str = str("".join(number))

    if any(
        [
            not digits_str.isdigit(),
            date_and_time[4] != "-",
            date_and_time[7] != "-",
            date_and_time[10] != "T",
            date_and_time[13] != ":",
            date_and_time[16] != ":",
            date_and_time[19] != ".",
        ]
    ):
        raise ValueError("Неправильный формат даты")

    return f"{date_and_time[8:10]}.{date_and_time[5:7]}.{date_and_time[:4]}"
