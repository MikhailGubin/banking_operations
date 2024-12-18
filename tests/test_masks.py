import pytest

from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize("card_number, expected", [("7000792289606361", "7000 79** **** 6361"),
                                                   ("1234567891011121", "1234 56** **** 1121"),
                                                   ("2365478912563489", "2365 47** **** 3489")])

def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


# @pytest.mark.parametrize("card_number, expected", [("7000792289606361", "7000 79** **** 6361"),
#                                                    ("1234567891011121", "1234 56** **** 1121"),
#                                                    ("2365478912563489", "2365 47** **** 3489")])

def test_get_mask_card_number_wrong_type():
    with pytest.raises(ValueError):
        get_mask_card_number([])


def test_get_mask_card_number_wrong_length():
    with pytest.raises(ValueError):
        get_mask_card_number(36547)

@pytest.mark.parametrize("account_number, expected", [("73654108430135874305", "**4305"),
                                                      ("12345678910111213569", "**3569"),
                                                      ("23654789125634894125", "**4125")])

def test_get_mask_account(account_number, expected):
    assert get_mask_account(account_number) == expected


def test_get_mask_account_wrong_type():
    with pytest.raises(ValueError):
        get_mask_account([])


def test_get_mask_account_wrong_length():
    with pytest.raises(ValueError):
        get_mask_account(36547)
