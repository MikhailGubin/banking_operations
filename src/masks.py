def get_mask_card_number(card_number: str|int) -> str:
    """Маскирует номер банковской карты."""
    card_number_str = str(card_number)
    if not card_number_str.isdigit() or len(card_number_str) != 16:
        raise ValueError("Неправильно введен номер карты")
    return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_number: str|int) -> str:
    """Маскирует номер банковского счета."""
    account_number_str = str(account_number)
    if not account_number_str.isdigit() or len(account_number_str) != 20:
        raise ValueError("Неправильно введен номер счёта")
    return "**" + account_number_str[-4:]
