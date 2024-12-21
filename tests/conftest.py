import pytest

@pytest.fixture
def banking_transactions() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:10:00.216451"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T08:55:30.512364"}
    ]


@pytest.fixture
def banking_transactions_no_given_state() -> list:
    return [
        {"id": 41428829, "state": "EXECUTE", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXCEPTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:10:00.216451"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
        ]


@pytest.fixture
def banking_transactions_no_state() -> list:
    return [
        {"id": 41428829, "state": "EXECUTE", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXCEPTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:10:00.216451"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
        ]