import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "account_card_number, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
    ],
)
def test_mask_account_card(account_card_number: str, expected: str) -> None:
    """ "
    Проверяет работу функции mask_account_card
    """
    assert mask_account_card(account_card_number) == expected


@pytest.mark.parametrize(
    "account_card_number",
    [
        "Maestro 159683",
        "Счет 646864736788947795895",
        "Счет 6831982476737658",
        "Visa Classic 64686473678894779589",
        "Visa Platinum ",
        "Счет ",
    ],
)
def test_mask_account_card_wrong_length(account_card_number: str) -> None:
    """ "
    Проверяет работу функции mask_account_card,
    когда на вход подаётся номер карты/счёта разной
    длины или когда номер отсутствует
    """
    with pytest.raises(ValueError):
        mask_account_card(account_card_number)
    # assert mask_account_card(account_card_number) == ""


@pytest.mark.parametrize(
    "account_card_number",
    [
        "1596837868705199 Maestro",
        "64686473678894779589 Счет",
        "MasterCard 71g830d734 26758",
        "Vilsa Classic 6831982476737658",
        "Maestroc 1596837868705199",
        "Счетс 73654108430135874305",
    ],
)
def test_mask_account_card_wrong_format(account_card_number: str) -> None:
    """ "
    Проверяет работу функции mask_account_card,
    когда на вход подаётся номер карты/счёта
    неправильного формата
    """
    with pytest.raises(ValueError):
        mask_account_card(account_card_number)
    # assert mask_account_card(account_card_number) == ""


@pytest.mark.parametrize(
    "date_and_time, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2002-05-21T00:13:12.632474", "21.05.2002"),
        ("2013-11-18T07:28:44.568762", "18.11.2013"),
    ],
)
def test_get_date(date_and_time: str, expected: str) -> None:
    """ "
    Проверяет работу функции get_date
    """
    assert get_date(date_and_time) == expected


@pytest.mark.parametrize(
    "date_and_time",
    [
        "2024-03-111T02:26:18",
        "2002-05-21T00:13",
        "2013-11-18L07:28:44.568762",
        "2013-11:18T07:28:44.568762",
        "2013411-18T07:28:44.568762",
        "",
    ],
)
def test_get_empty_date_wrong_format(date_and_time: str) -> None:
    """ "
    Проверяет работу функции get_date при различных
    неправильных входных форматах
    """
    with pytest.raises(ValueError):
        get_date(date_and_time)
