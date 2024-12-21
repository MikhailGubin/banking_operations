import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state, expected",
[("EXECUTED", [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T08:55:30.512364"}
    ]),
("CANCELED",[
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:10:00.216451"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ])])
def test_filter_by_different_state(banking_transactions: list, state: str, expected: list) -> None:
    """"
    Проверяет работу функции filter_by_state со словарями с различными возможными
    значениями статуса state
    """
    assert filter_by_state(banking_transactions, state) == expected


def test_filter_by_state(banking_transactions_no_given_state: list) -> None:
    """"
    Проверяет работу функции filter_by_state при отсутствии словарей с указанным
    статусом state в списке
    """
    with pytest.raises(ValueError):
        filter_by_state(banking_transactions_no_given_state)


def test_filter_without_state(banking_transactions_no_state: list) -> None:
    """"
    Проверяет работу функции filter_by_state со словарями без
    статуса state в списке
    """
    with pytest.raises(ValueError):
        filter_by_state(banking_transactions_no_state)


@pytest.mark.parametrize("decreasing_meaning, expected",
    [(True, [
        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'},
        {'date': '2018-10-14T08:10:00.216451', 'id': 615064591, 'state': 'CANCELED'},
        {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
        {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
        {'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'},
        {'date': '2019-07-03T08:55:30.512364', 'id': 41428829, 'state': 'EXECUTED'}
    ]),
    (False,[
        {'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'},
        {'date': '2019-07-03T08:55:30.512364', 'id': 41428829, 'state': 'EXECUTED'},
        {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
        {'date': '2018-10-14T08:10:00.216451', 'id': 615064591, 'state': 'CANCELED'},
        {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}])
    ])
def test_sort_by_date(banking_transactions: list, decreasing_meaning: bool, expected: list) -> None:
    """"
    Тестирует сортировку списка словарей по датам в порядке убывания и возрастания
    и проверяет корректность сортировки при одинаковых датах
    """
    assert sort_by_date(banking_transactions, decreasing=decreasing_meaning) == expected


@pytest.mark.parametrize("banking_transactions_wrong_format",
    [
{'date': '-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'},
        {'date': '2018--14T08:10:00.216451', 'id': 615064591, 'state': 'CANCELED'},
        {'date': '2018-10-T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
        {'date': '2018-09-1221:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
        {'date': '2019-07-03T', 'id': 41428829, 'state': 'EXECUTED'},
        {'date': 'T08:55:30512364', 'id': 41428829, 'state': 'EXECUTED'},
        {'date': '2019-027-03518:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'},
        {'date': '', 'id': 41428829, 'state': 'EXECUTED'},
        {'id': 594226727, 'state': 'CANCELED'}
    ])

def test_sort_by_date(banking_transactions_wrong_format: list) -> None:
    """"
    Проверяет работу функции sort_by_date с некорректными
     или нестандартными форматами дат
    """
    with pytest.raises(ValueError):
        sort_by_date(banking_transactions_wrong_format)
