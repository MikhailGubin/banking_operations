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
def test_filter_by_state(banking_transactions: list, state: str, expected: list) -> None:
    """"
    Проверяет работу функции filter_by_state
    """
    assert filter_by_state(banking_transactions, state) == expected


@pytest.mark.parametrize("decreasing_meaning, expected",
    [(True, [
    {'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'},
    {'date': '2019-07-03T08:55:30.512364', 'id': 41428829, 'state': 'EXECUTED'},
    {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
    {'date': '2018-10-14T08:10:00.216451', 'id': 615064591, 'state': 'CANCELED'},
    {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
    {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'}
            ]),
    (False,[
        {'date': '2018-06-30T02:08:58.425572', 'id': 939719570, 'state': 'EXECUTED'},
        {'date': '2018-09-12T21:27:25.241689', 'id': 594226727, 'state': 'CANCELED'},
        {'date': '2018-10-14T08:10:00.216451', 'id': 615064591, 'state': 'CANCELED'},
        {'date': '2018-10-14T08:21:33.419441', 'id': 615064591, 'state': 'CANCELED'},
        {'date': '2019-07-03T08:55:30.512364', 'id': 41428829, 'state': 'EXECUTED'},
        {'date': '2019-07-03T18:35:29.512364', 'id': 41428829, 'state': 'EXECUTED'}
            ])
    ])
def test_sort_by_date(banking_transactions: list, decreasing_meaning: bool, expected: list) -> None:
    """"
    Проверяет работу функции filter_by_state
    """
    assert sort_by_date(banking_transactions, decreasing=decreasing_meaning) == expected