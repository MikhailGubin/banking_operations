import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("7000792289606361", "7000 79** **** 6361"),
        ("1234567891011121", "1234 56** **** 1121"),
        (2365478912563489, "2365 47** **** 3489"),
    ],
)
def test_get_mask_card_number(card_number: str | int, expected: str) -> None:
    """ "
    Проверяет работу функции get_mask_card_number
    """
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("card_number", [(["7000792289606361"]), ({"12345 7891011121"}), (True)])
def test_get_mask_card_number_wrong_type(card_number: str | int) -> None:
    """ "
    Проверяет работу функции get_mask_card_number,
    когда на вход подаются данные другого типа
    """
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize("card_number", [("70007922896063611258"), ("1234"), ("")])
def test_get_mask_card_number_wrong_length(card_number: str | int) -> None:
    """ "
    Проверяет работу функции get_mask_card_number,
    когда на вход подаётся номер карты другого размера
    или отсутствует
    """
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)


@pytest.mark.parametrize(
    "account_number, expected",
    [("73654108430135874305", "**4305"), ("12345678910111213569", "**3569"), (23654789125634894125, "**4125")],
)
def test_get_mask_account(account_number: str | int, expected: str) -> None:
    """ "
    Проверяет работу функции get_mask_account
    """
    assert get_mask_account(account_number) == expected


@pytest.mark.parametrize("account_number", [(["70007922896063614759"]), ({"123456789 0111213569"}), (True)])
def test_get_mask_account_wrong_type(account_number: str | int) -> None:
    """ "
    Проверяет работу функции get_mask_account,
     когда на вход подаются данные другого типа
    """
    with pytest.raises(ValueError):
        get_mask_account(account_number)


@pytest.mark.parametrize("account_number", [("7365410843013587430556"), ("1234567569"), ("")])
def test_get_mask_account_wrong_length(account_number: str | int) -> None:
    """ "
    Проверяет работу функции get_mask_account,
    когда на вход подаётся номер счёта другого размера или номер отсутствует
    """
    with pytest.raises(ValueError):
        get_mask_account(account_number)
