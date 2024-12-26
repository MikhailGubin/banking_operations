import pytest

from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.mark.parametrize(
    "currency, expected",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
        ),
        (
            "RUB",
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160",
                },
                {
                    "id": 594226727,
                    "state": "CANCELED",
                    "date": "2018-09-12T21:27:25.241689",
                    "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод организации",
                    "from": "Visa Platinum 1246377376343588",
                    "to": "Счет 14211924144426031657",
                },
            ],
        ),
    ],
)
def test_filter_by_currency(transactions_for_generate: list, currency: str, expected: list) -> None:
    """ "
    Проверяет, что функция-генератор filter_by_currency
    корректно фильтрует по заданному значению валюты
    """
    currency_transactions = filter_by_currency(transactions_for_generate, currency)
    amount_iterations = 0
    for transaction in transactions_for_generate:
        if "code" not in transaction["operationAmount"]["currency"]:
            continue
        if transaction["operationAmount"]["currency"]["code"] == currency:
            amount_iterations += 1

    for iteration in range(amount_iterations):
        assert next(currency_transactions) == expected[iteration]


def test_filter_by_currency_empty_list() -> None:
    """ "
    Проверяет, что функция filter_by_currency корректно
    работает при передаче ей пустого списка. Также проверяет,
    что программа не завершается ошибкой после окончания работы
    генератора
    """
    empty_transaction = filter_by_currency([])
    assert next(empty_transaction) == "Пустой список транзакций"
    assert next(empty_transaction) == "Генератор закончил работу"


def test_filter_by_no_currency_in_list(transactions_for_generate: list, currency: str = "EURO") -> None:
    """ "
    Проверяет, что функция-генератор filter_by_currency
    корректно работает при передаче ей списка, где нет
    заданной валюты
    """
    no_necessary_transaction = filter_by_currency(transactions_for_generate, currency)
    assert next(no_necessary_transaction) == "Транзакции в заданной валюте отсутствуют"
    assert next(no_necessary_transaction) == "Генератор закончил работу"


@pytest.mark.parametrize(
    "expected",
    [
        (
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
                "Перевод организации",
                "Перевод организации",
            ]
        )
    ],
)
def test_transaction_descriptions(transactions_for_generate: list, expected: str) -> str:
    """ "
    Проверяет работу генератора transaction_descriptions
    """
    descriptions = transaction_descriptions(transactions_for_generate)
    for index in range(6):
        assert next(descriptions) == expected[index]

    assert next(descriptions) == "Генератор закончил работу"


def test_no_transaction_descriptions(transactions_for_generate: list) -> str:
    """ "
    Проверяет работу функции-генератора
    transaction_descriptions при передаче ей пустого
    списка
    """
    descriptions = transaction_descriptions([])
    assert next(descriptions) == "Пустой список транзакций"
    assert next(descriptions) == "Генератор закончил работу"


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
            1111111111111111,
            1111111111111115,
            [
                "1111 1111 1111 1111",
                "1111 1111 1111 1112",
                "1111 1111 1111 1113",
                "1111 1111 1111 1114",
                "1111 1111 1111 1115",
            ],
        ),
        (
            11,
            19,
            [
                "0000 0000 0000 0011",
                "0000 0000 0000 0012",
                "0000 0000 0000 0013",
                "0000 0000 0000 0014",
                "0000 0000 0000 0015",
                "0000 0000 0000 0016",
                "0000 0000 0000 0017",
                "0000 0000 0000 0018",
                "0000 0000 0000 0019",
            ],
        ),
    ],
)
def test_card_number_generator(start: int, stop: int, expected: list) -> None:
    """
    Проверяет работы функции-генератора
    card_number_generator
    """
    card_number = card_number_generator(start, stop)

    for index in range(stop - start + 1):
        assert next(card_number) == expected[index]


@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (-1, 10, "Диапазон чисел меньше 0"),
        (10, -1, "Диапазон чисел меньше 0"),
        (1, 1, "Начало и конец диапазона совпадают"),
        (999999999999999, 99999999999999999, "Диапазон чисел вышел за верхнюю границу"),
    ],
)
def test_card_number_generator_wrong_cases(start: int, stop: int, expected: list) -> None:
    """
    Проверяет работы функции-генератора
    card_number_generator, когда на вход
    были переданы неправильные данные
    """
    card_number = card_number_generator(start, stop)
    assert next(card_number) == expected
